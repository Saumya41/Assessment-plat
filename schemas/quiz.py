from pydantic import BaseModel
from typing import List, Optional, Any

class QuestionSchema(BaseModel):
    question_text: str
    options: List[str]

class QuizResponseSchema(BaseModel):
    title: Optional[str]
    questions: List[QuestionSchema]

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[QuizResponseSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": {
                    "title": "Sample Quiz",
                    "questions": [
                        {
                            "question_text": "What is the capital of France?",
                            "options": ["Paris", "London", "Berlin", "Madrid"]
                        }
                    ]
                }
            }
        }

class StudentScore(BaseModel):
    quiz_id: str
    student_id: str
    score: int

    class Config:
        orm_mode = True
