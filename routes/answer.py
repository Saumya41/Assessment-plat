from fastapi import APIRouter, Body, HTTPException
from beanie import PydanticObjectId

from models.answer import UniversalAnswer, StudentAnswer
from schemas.answer import UniversalAnswerSchema, StudentAnswerSchema
from database.database import add_universal_answer, add_student_answer, retrieve_universal_answer, retrieve_student_answers, calculate_score
from fastapi import APIRouter, HTTPException, Depends
from schemas.score import ScoreResponse  # Create a schema for the score response


router = APIRouter()


# Universal Answer Route
@router.post("/universal_answer", response_description="Add the correct answer to a question")
async def add_universal_answer_data(answer_data: UniversalAnswerSchema = Body(...)):
    universal_answer = UniversalAnswer(**answer_data.dict())
    new_answer = await add_universal_answer(universal_answer)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Universal answer added successfully",
        "data": new_answer,
    }


# Student Answer Route
@router.post("/student_answer", response_description="Record student's answer")
async def add_student_answer_data(answer_data: StudentAnswerSchema = Body(...)):
    student_answer = StudentAnswer(**answer_data.dict())
    new_answer = await add_student_answer(student_answer)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student answer recorded successfully",
        "data": new_answer,
    }


# Retrieve Universal Answer by Question ID
@router.get("/universal_answer/{question_id}", response_description="Get the correct answer for a question")
async def get_universal_answer(question_id: PydanticObjectId):
    answer = await retrieve_universal_answer(question_id)
    if answer:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Universal answer retrieved successfully",
            "data": answer,
        }
    raise HTTPException(status_code=404, detail="Universal answer not found")


# Retrieve Student Answers by Quiz ID and User ID
@router.get("/student_answers/{quiz_id}/{user_id}", response_description="Get student's answers for a quiz")
async def get_student_answers(quiz_id: PydanticObjectId, user_id: PydanticObjectId):
    answers = await retrieve_student_answers(quiz_id, user_id)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student answers retrieved successfully",
        "data": answers,
    }



@router.get("/quiz/{quiz_id}/student/{student_id}/score", response_model=ScoreResponse)
async def get_student_score(quiz_id: PydanticObjectId, student_id: PydanticObjectId):
    try:
        score = await calculate_score(quiz_id, student_id)
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Score calculated successfully",
            "score": score
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
