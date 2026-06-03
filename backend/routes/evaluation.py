from fastapi import APIRouter

router = APIRouter()

@router.get("/evaluation-test")
def evaluation_test():

    return {
        "message": "Evaluation API Working"
    }