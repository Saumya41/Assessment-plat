from pydantic import BaseModel, EmailStr
from typing import Optional, Any

class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Collection:
        name = "student"

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Saumya",
                "email": "saumya@school.com",
                "course_of_study": "b.tech engineering",
                "year": 4,
                "gpa": "0",
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
