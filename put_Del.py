from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):

    patient_id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female'], Field(..., description='Gender of the patient')]
    blood_group: Annotated[str, Field(..., description='Blood group of the patient')]
    symptoms: Annotated[list[str], Field(..., description='Symptoms of the patient')]
    blood_pressure: Annotated[str, Field(..., description='Blood pressure of the patient')]
    heart_rate: Annotated[int, Field(..., gt=0, description='Heart rate of the patient')]
    temperature_c: Annotated[float, Field(..., description='Body temperature in Celsius')]
    diagnosis: Annotated[str, Field(..., description='Diagnosis of the patient')]
    medications: Annotated[list[str], Field(..., description='Medications of the patient')]
    allergies: Annotated[list[str], Field(..., description='Allergies of the patient')]


class PatientUpdate(BaseModel):

    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    blood_group: Annotated[Optional[str], Field(default=None)]
    symptoms: Annotated[Optional[list[str]], Field(default=None)]
    blood_pressure: Annotated[Optional[str], Field(default=None)]
    heart_rate: Annotated[Optional[int], Field(default=None, gt=0)]
    temperature_c: Annotated[Optional[float], Field(default=None)]
    diagnosis: Annotated[Optional[str], Field(default=None)]
    medications: Annotated[Optional[list[str]], Field(default=None)]
    allergies: Annotated[Optional[list[str]], Field(default=None)]


def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)

    return data


def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f, indent=4)


@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}


@app.get('/view')
def view():
    data = load_data()

    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):

    data = load_data()

    for patient in data:
        if patient['patient_id'] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of age, heart_rate or temperature_c'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['age', 'heart_rate', 'temperature_c']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()

    for existing_patient in data:
        if existing_patient['patient_id'] == patient.patient_id:
            raise HTTPException(status_code=400, detail='Patient already exists')

    data.append(patient.model_dump())

    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    for patient in data:

        if patient['patient_id'] == patient_id:

            updated_patient_info = patient_update.model_dump(exclude_unset=True)

            for key, value in updated_patient_info.items():
                patient[key] = value

            save_data(data)

            return JSONResponse(status_code=200, content={'message': 'patient updated'})

    raise HTTPException(status_code=404, detail='Patient not found')


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    for patient in data:

        if patient['patient_id'] == patient_id:

            data.remove(patient)

            save_data(data)

            return JSONResponse(status_code=200, content={'message': 'patient deleted'})

    raise HTTPException(status_code=404, detail='Patient not found')