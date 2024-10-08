from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class Student(Document):
    fullname: str
    email: EmailStr
    course_of_study: str
    year: int
    gpa: float

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Saumya",
                "email": "saumya@school.com",
                "course_of_study": "B.tech engineering",
                "year": 4,
                "gpa": "8.0",
            }
        }

    class Settings:
        name = "student"
