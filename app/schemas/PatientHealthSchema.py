from pydantic import BaseModel


class PatientHealthSchema(BaseModel):
    allergies: list
    current_medications: list
    other_comments: str


class GetHealthStatus(BaseModel):
    data = "True/False"
