from fastapi import APIRouter

router = APIRouter()

@router.get("/interview-test")
def interview_test():

    return {
        "message": "Interview API Working"
    }   