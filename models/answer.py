from beanie import Document, PydanticObjectId
from pydantic import Field

class UniversalAnswer(Document):
    question_id: PydanticObjectId
    correct_answer: str

    class Settings:
        name = "universal_answers"


class StudentAnswer(Document):
    quiz_id: PydanticObjectId
    student_id: PydanticObjectId
    question_id: PydanticObjectId
    student_answer: str

    class Settings:
        name = "student_answers"
