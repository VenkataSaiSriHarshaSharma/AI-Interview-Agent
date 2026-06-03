from pydantic import BaseModel

class InterviewRequest(BaseModel):

    role: str
    question_count: int