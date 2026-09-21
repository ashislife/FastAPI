from pydantic import BaseModel 

# step1:create a class of pydantic model 
# inside the class types validation 
class Patient(BaseModel):
    name:str
    age:int

# step2:create a object of the class

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)

    print("inserted patient data") 

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)

    print("updated patient data")


patient_info={'name':'Ashish','age':20}

patient1=Patient(**patient_info)


# step3:print the object of the class
insert_patient_data(patient1)


# update_patient_data(patient1)


# NOTe:
# if i pass the wrong data type (for example age='20' then output will be integer automatically )