from pydantic import BaseModel
from beanie import PydanticObjectId
from typing import Optional

class UniversalAnswerSchema(BaseModel):
    question_id: PydanticObjectId
    correct_answer: str

    class Config:
        json_schema_extra = {
            "example": {
                "question_id": "66b13628b99d99505231c5d6",
                "correct_answer": "Paris",
            }
        }
    class Collection:
        name = "universal_answer"
    


class StudentAnswerSchema(BaseModel):
    quiz_id: PydanticObjectId
    Student_id: PydanticObjectId
    question_id: PydanticObjectId
    student_answer: str

    class Config:
        json_schema_extra = {
            "example": {
                "quiz_id": "64d5f87cf00f080014c4a5e4",
                "student_id": "64d5f87cf00f080014c4a5e6",
                "question_id": "64d5f87cf00f080014c4a5e5",
                "student_answer": "Paris",
            }
        }
    class Collection:
        name = "student_answer"
