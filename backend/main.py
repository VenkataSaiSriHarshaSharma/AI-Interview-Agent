from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.resume import router as resume_router
from backend.routes.interview import router as interview_router
from backend.routes.evaluation import router as evaluation_router

app = FastAPI(
    title="AI Recruitment API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    resume_router,
    prefix="/api"
)

app.include_router(
    interview_router,
    prefix="/api"
)

app.include_router(
    evaluation_router,
    prefix="/api"
)

@app.get("/")
def home():

    return {
        "status": "running",
        "service": "AI Recruitment API"
    }