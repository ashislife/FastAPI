from pydantic import BaseModel ,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional

# Here email automatically validate if we use build in pydantic model EmailStr
# we use AnyUrl for url validation 
# custom data validation using Field (weight always be positive )

class Patient(BaseModel):
    name:str
    email:EmailStr
    linkdin_url:AnyUrl
    age:int
    weight:float=Field(gt=0)
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
    print(patient.email)
    print(patient.linkdin_url)

    print("updated patient data")

patient_info={'name':'Ashish','email':'ashishk@gmail.com','linkdin_url':'https://www.linkedin.com/in/ashishk','age':20,'weight':50.0,'allergies':['dust','pollen'],'contact_details':{'phone':'7484002145'}}

patient1=Patient(**patient_info)
update_patient_data(patient1)