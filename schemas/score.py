from pydantic import BaseModel

class ScoreResponse(BaseModel):
    status_code: int
    response_type: str
    description: str
    score: int
