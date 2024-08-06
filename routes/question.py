from fastapi import APIRouter, Body, HTTPException
from beanie import PydanticObjectId

from database.database import *
from models.question import Question
from schemas.question import Response, UpdateQuestionModel

router = APIRouter()

@router.get("/", response_description="Questions retrieved", response_model=Response)
async def get_questions():
    questions = await retrieve_questions()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Questions data retrieved successfully",
        "data": questions,
    }

@router.get("/{id}", response_description="Question data retrieved", response_model=Response)
async def get_question_data(id: PydanticObjectId):
    question = await retrieve_question(id)
    if question:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Question data retrieved successfully",
            "data": question,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Question doesn't exist",
    }

@router.post(
    "/",
    response_description="Question data added into the database",
    response_model=Response,
)
async def add_question_data(question: Question = Body(...)):
    new_question = await add_question(question)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Question created successfully",
        "data": new_question,
    }

@router.delete("/{id}", response_description="Question data deleted from the database")
async def delete_question_data(id: PydanticObjectId):
    deleted_question = await delete_question(id)
    if deleted_question:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Question with ID: {} removed".format(id),
            "data": deleted_question,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Question with id {0} doesn't exist".format(id),
        "data": False,
    }

@router.put("/{id}", response_model=Response)
async def update_question(id: PydanticObjectId, req: UpdateQuestionModel = Body(...)):
    updated_question = await update_question_data(id, req.dict())
    if updated_question:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Question with ID: {} updated".format(id),
            "data": updated_question,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Question with ID: {} not found".format(id),
        "data": False,
    }

@router.post("/create_quiz", response_description="Create a quiz from selected questions")
async def create_quiz_endpoint(question_ids: List[PydanticObjectId] = Body(...)):
    questions = await create_quiz(question_ids)
    if not questions:
        raise HTTPException(status_code=404, detail="Questions not found")
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Quiz created successfully",
        "data": questions,
    }
