from fastapi import APIRouter, Body, HTTPException
from typing import List
from beanie import PydanticObjectId
from database.database import retrieve_questions_by_ids, create_quiz
from schemas.quiz import Response, QuizCreate

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
