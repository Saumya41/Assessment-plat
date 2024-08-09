from pydantic import BaseModel
from typing import List, Optional, Any

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

class StudentScore(BaseModel):
    quiz_id: str
    student_id: str
    score: int

    class Config:
        orm_mode = True
