from typing import Optional, List
from beanie import Document, PydanticObjectId

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
