from typing import Optional, Any, List

from beanie import Document
from pydantic import BaseModel

class Question(Document):
    question_text: str
    options: List[str]
    correct_answer: str

    

    class Config:
        json_schema_extra = {
            "example": {
                "question_text": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris",
            }
        }
    class Settings:
        name = "question"  # Ensure this matches your collection name in MongoDB
