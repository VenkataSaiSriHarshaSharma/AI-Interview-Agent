from fastapi import APIRouter
from pydantic import BaseModel

from agents import (
    evaluate_interview
)

model = None

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