from typing import List, Union
from beanie import PydanticObjectId
from beanie import init_beanie
from models.admin import Admin
from models.student import Student
from models.question import Question
from models.answer import UniversalAnswer, StudentAnswer

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



async def create_quiz(question_ids: List[PydanticObjectId]) -> List[Question]:
    # Retrieve questions based on the provided IDs
    questions = await Question.find(Question.id.in_(question_ids)).to_list()
    return questions




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
