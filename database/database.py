from typing import List, Union, Dict
from beanie import PydanticObjectId
from models.admin import Admin
from models.student import Student
from models.question import Question
from models.answer import UniversalAnswer, StudentAnswer
from models.quiz import Quiz, StudentScore
from models.answer import StudentAnswer, UniversalAnswer

admin_collection = Admin
student_collection = Student
question_collection = Question



async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


async def retrieve_students() -> List[Student]:
    students = await student_collection.all().to_list()
    return students


async def add_student(new_student: Student) -> Student:
    student = await new_student.create()
    return student


async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student


async def delete_student(id: PydanticObjectId) -> bool:
    student = await student_collection.get(id)
    if student:
        await student.delete()
        return True


async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    student = await student_collection.get(id)
    if student:
        await student.update(update_query)
        return student
    return False



async def retrieve_questions() -> List[Question]:
    questions = await question_collection.all().to_list()
    return questions


async def add_question(new_question: Question) -> Question:
    question = await new_question.create()
    return question


async def retrieve_question(id: PydanticObjectId) -> Question:
    question = await question_collection.get(id)
    if question:
        return question


async def delete_question(id: PydanticObjectId) -> bool:
    question = await question_collection.get(id)
    if question:
        await question.delete()
        return True


async def update_question_data(id: PydanticObjectId, data: dict) -> Union[bool, Question]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    question = await question_collection.get(id)
    if question:
        await question.update(update_query)
        return question
    return False


async def retrieve_questions_by_ids(question_ids: List[PydanticObjectId]) -> List[Question]:
    questions = await Question.find({"_id": {"$in": question_ids}}).to_list()
    return questions


async def create_quiz(question_ids: List[PydanticObjectId], title: str = None) -> Quiz:
    quiz = Quiz(title=title, questions=question_ids)
    await quiz.insert()
    return quiz

# Universal Answer
async def add_universal_answer(answer: UniversalAnswer) -> UniversalAnswer:
    return await answer.create()


async def retrieve_universal_answer(question_id: PydanticObjectId) -> UniversalAnswer:
    return await UniversalAnswer.find_one(UniversalAnswer.question_id == question_id)


# Student Answer
async def add_student_answer(answer: StudentAnswer) -> StudentAnswer:
    return await answer.create()


async def retrieve_student_answers(quiz_id: PydanticObjectId, user_id: PydanticObjectId) -> List[StudentAnswer]:
    return await StudentAnswer.find(StudentAnswer.quiz_id == quiz_id, StudentAnswer.user_id == user_id).to_list()


async def calculate_score(quiz_id: PydanticObjectId, student_id: PydanticObjectId) -> int:
    # Retrieve the student's answers for the given quiz
    student_answers: List[StudentAnswer] = await retrieve_student_answers(quiz_id, student_id)
    
    # Initialize the score
    score = 0
    
    # Iterate over the student's answers
    for student_answer in student_answers:
        question_id = student_answer.question_id
        
        # Retrieve the correct (universal) answer for this question
        correct_answer_doc: UniversalAnswer = await retrieve_universal_answer(question_id)
        
        if correct_answer_doc is None:
            # If no correct answer is found, log this case or handle it accordingly
            continue  # Skip this question and move to the next
        
        correct_answer = correct_answer_doc.correct_answer
        
        # Normalize both strings: strip whitespace and convert to lowercase for comparison
        if correct_answer.strip().lower() == student_answer.student_answer.strip().lower():
            score += 1

    # Save the score in the database
    await save_student_score(quiz_id, student_id, score)

    return score
async def retrieve_quiz_by_id(quiz_id: PydanticObjectId) -> Quiz:
    quiz = await Quiz.get(quiz_id)
    return quiz

async def save_student_score(quiz_id: PydanticObjectId, student_id: PydanticObjectId, score: int) -> None:
    # Create a new StudentScore document
    student_score = StudentScore(
        quiz_id=quiz_id,
        student_id=student_id,
        score=score
    )
    
    # Save the document to the database
    await student_score.insert()

async def retrieve_student_score(quiz_id: PydanticObjectId, student_id: PydanticObjectId) -> StudentScore:
    student_score = await StudentScore.find_one({"quiz_id": quiz_id, "student_id": student_id})
    return student_score