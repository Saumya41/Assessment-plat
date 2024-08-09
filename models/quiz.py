from typing import Optional, List
from beanie import Document, PydanticObjectId
from pydantic import BaseModel


class Quiz(Document):
    title: Optional[str] = None
    questions: List[PydanticObjectId]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Geography Quiz",
                "questions": ["60adf2df5d2a2c1a94d7f20b", "60adf2df5d2a2c1a94d7f20c"],
            }
        }

    class Settings:
        name = "quiz"



class StudentScore(Document):
    quiz_id: PydanticObjectId  # The ID of the quiz
    student_id: PydanticObjectId  # The ID of the student
    score: int  # The score the student achieved

    class Config:
        json_schema_extra = {
            "example": {
                "quiz_id": "64df9f8e5b36a9d7ac8b4567",
                "student_id": "64df9f8e5b36a9d7ac8b4568",
                "score": 90,
            }
        }
    
    class Settings:
        name = "student_scores"  # Collection name in MongoDB

