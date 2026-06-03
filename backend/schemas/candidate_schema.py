from pydantic import BaseModel

class Candidate(BaseModel):

    name: str
    role: str
    experience: str