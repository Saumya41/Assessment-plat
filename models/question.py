from typing import Optional, Any, List
from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from bson import ObjectId

class Question(Document):
    question_text: str
    options: List[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "question_text": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                
            }
        }
    class Settings:
        name = "question"  # Ensure this matches your collection name in MongoDB