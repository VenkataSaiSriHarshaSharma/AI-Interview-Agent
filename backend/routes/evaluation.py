from fastapi import APIRouter
from pydantic import BaseModel

from agents import evaluate_interview
from backend.database import reports_collection

router = APIRouter()

model = None


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

    report_data = {
        "candidate_profile":
            data.candidate_profile,
        "answers":
            data.answers,
        "report":
            report
    }

    try:

        reports_collection.insert_one(
            report_data
        )

        print(
            "MongoDB Save Success"
        )

    except Exception as e:

        print(
            "MongoDB Save Failed:",
            str(e)
        )

    return {
        "report": report
    }