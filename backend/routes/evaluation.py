from fastapi import APIRouter
from pydantic import BaseModel

from agents import (
    evaluate_interview
)

from backend.services.gemini_service import (
    model
)

router = APIRouter()


class EvaluationRequest(BaseModel):

    candidate_profile: dict
    answers: list


@router.post("/evaluate")
def evaluate_candidate(
    data: EvaluationRequest
):

    report = evaluate_interview(
        data.candidate_profile,
        data.answers,
        model
    )

    return {
        "report": report
    }