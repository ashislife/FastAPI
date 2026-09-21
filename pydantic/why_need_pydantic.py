def insert_patient_data(name,age):

    print(name)
    print(age)

    print("inserted patient data")
insert_patient_data('Ashish','twenty')

# --------------------used typed hinting -------------------

def insert_patient_data(name:str,age:int):

    print(name)
    print(age)

    print("inserted patient data")
insert_patient_data('Ashish','30')



# strickly enforce the code to accept only the data type we want to accept
def insert_patient_data(name,age):

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("inserted patient data")
    else:
        raise TypeError("Invalid data type")
insert_patient_data('Ashish',20)