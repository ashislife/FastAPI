from fastapi import FastAPI
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