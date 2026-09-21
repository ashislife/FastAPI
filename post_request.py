from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel, Field
from typing import Annotated, Literal


app = FastAPI()


class Patient(BaseModel):
    patient_id: str
    age: Annotated[int, Field(gt=0, le=120)]
    gender: Annotated[
        Literal['male', 'female', 'other'],
        Field(description="Gender of the patient")
    ]
    blood_group: str
    symptoms: list[str]
    blood_pressure: str
    heart_rate: Annotated[int, Field(gt=0, le=250)]
    temperature_c: Annotated[float, Field(gt=30, lt=45)]
    diagnosis: str
    medications: list[str]
    allergies: list[str]


def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data


@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()

    # Check if patient_id already exists
    for p in data:
        if p['patient_id'] == patient.patient_id:
            raise HTTPException(
                status_code=400,
                detail=f"Patient with id {patient.patient_id} already exists"
            )

    # Add new patient
    data.append(patient.model_dump())

    # Save updated data
    with open('patient.json', 'w') as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Patient created successfully",
        "patient": patient.model_dump()
    }