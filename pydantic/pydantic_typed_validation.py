from pydantic import BaseModel 
from typing import List,Dict,Optional
# optional ->we are not req to pass the value of the field (if i not passed then it will be None)

class Patient(BaseModel):
    name:str
    age:int
    weight:float=False
    married:Optional[bool]=None 
    allergies:Optional[List[str]]=None 
    contact_details:Dict[str,str]



def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)

    print("inserted patient data") 

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.weight)

    print("updated patient data")

patient_info={'name':'Ashish','age':20,'allergies':['dust','pollen'],'contact_details':{'email': 'ashishk00047@gmail.com','phone':'7484002145'}}

patient1=Patient(**patient_info)
update_patient_data(patient1)