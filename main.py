from fastapi import FastAPI 

app=FastAPI()  #object 

@app.get("/")  #decorator to define a GET endpoint at the root URL
def read_root():  #function to handle GET requests to the root URL
    return {"message": "Hello, World!"}  #returns a JSON response 

@app.get("/about")
def about_msg():
    return {"message":"A FASTAPI application "}