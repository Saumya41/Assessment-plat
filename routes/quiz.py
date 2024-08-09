from fastapi import APIRouter, Body, HTTPException
from typing import List
from beanie import PydanticObjectId
from database.database import retrieve_questions_by_ids, create_quiz, retrieve_student
from schemas.quiz import Response, QuizCreate
from utils.email import send_assessment_email
from models.student import Student
from schemas.student import Response, UpdateStudentModel
from utils.utils import generate_assessment_link
router = APIRouter()

@router.post("/create_quiz", response_description="Create a quiz from selected questions", response_model=Response)
async def create_quiz_endpoint(question_ids: List[PydanticObjectId] = Body(...), title: str = Body(None)):
    questions = await retrieve_questions_by_ids(question_ids)
    if not questions:
        raise HTTPException(status_code=404, detail="Some questions were not found.")
    
    quiz = await create_quiz(question_ids=question_ids, title=title)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Quiz created successfully",
        "data": quiz,
    }

@router.post("/send-assessment-link/{student_id}/{quiz_id}")
async def send_assessment_link(student_id: str, quiz_id: str):
    student = await retrieve_student(student_id)  # Fetch student from the database
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    assessment_link = generate_assessment_link(student_id, quiz_id)  # Pass both student_id and quiz_id
    send_assessment_email(student.email, assessment_link)  # Assuming this function is defined elsewhere
    
    return {"message": "Assessment link sent successfully."}
