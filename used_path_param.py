from fastapi import FastAPI,Path
import json

app=FastAPI()

# load the Json data
def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
    return data 


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'Message':'A fully functional API to manage patient records'}


# view all data from json file 
@app.get("/view")
def view():
    data=load_data()
    return data



# using path parameter to get a specific patient record by ID
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient in DB",example="P001")):
    data = load_data()

    for patient in data:
        if patient["patient_id"] == patient_id:
            return patient

    return {"message": "Patient not found"}