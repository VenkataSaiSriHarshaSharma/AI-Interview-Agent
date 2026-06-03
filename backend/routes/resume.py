from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import os
import tempfile

from resume_parser import (
    extract_resume_text
)

from agents import (
    screen_resume
)

from backend.services.gemini_service import (
    model
)

router = APIRouter()


@router.post("/screen-resume")
async def screen_resume_api(
    role: str = Form(...),
    resume: UploadFile = File(...)
):

    try:

        resume_text = extract_resume_text(
            resume
        )

        report = screen_resume(
            resume_text,
            role,
            model
        )

        return {

            "success": True,
            "role": role,
            "report": report

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }