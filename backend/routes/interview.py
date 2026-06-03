from fastapi import APIRouter
from pydantic import BaseModel

from question_bank import (
    generate_random_questions
)

router = APIRouter()

class InterviewRequest(BaseModel):
    role: str
    question_count: int


@router.post("/generate-questions")
def generate_questions(
    data: InterviewRequest
):

    questions = generate_random_questions(
        data.role,
        data.question_count
    )

    return {
        "questions": questions
    }