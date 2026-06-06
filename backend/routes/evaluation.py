from fastapi import APIRouter
from pydantic import BaseModel

from agents import evaluate_interview
from backend.database import reports_collection

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

    report_data = {
        "candidate_profile":
            data.candidate_profile,
        "answers":
            data.answers,
        "report":
            report
    }

    reports_collection.insert_one(
        report_data
    )

    return {
        "report": report
    }

@router.get("/reports")
def get_reports():

    reports = []

    for item in reports_collection.find():

        item["_id"] = str(
            item["_id"]
        )

        reports.append(item)

    return reports