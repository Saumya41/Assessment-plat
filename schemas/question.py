from pydantic import BaseModel
from typing import List, Optional, Any

class UpdateQuestionModel(BaseModel):
    question_text: Optional[str]
    options: List[str]
    

    class Collection:
        name = "question"

    class Config:
        json_schema_extra = {
            "example": {
                "question_text": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }

class QuizCreate(BaseModel):
    title: Optional[str]
    question_ids: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Sample Quiz",
                "question_ids": ["60adf2df5d2a2c1a94d7f20b", "60adf2df5d2a2c1a94d7f20c"],
            }
        }
