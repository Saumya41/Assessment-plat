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
