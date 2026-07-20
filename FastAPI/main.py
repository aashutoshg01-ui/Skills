from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message from home page": "Hello Aashutosh using venv"}

# About Route
@app.get("/about")
def about():
    return {"message": "This is about page"}

# Users Route using path parameters
@app.get("/users/{user_id}")
def get_user (user_id : int):
    return {"user_id" : user_id}

# Users Route using Query parameters
@app.get("/users")
def get_user (name : str = None):
    return {"Name" : name}

#Experiment
@app.get("/user/{user_id}")
def get_user (user_id, name):
    return {"user_id" : user_id ,  "Name" : name}

#Default Value using Query Parameters
@app.get("/products")
def get_user (limit : int = 10):
    return {"limit" : limit}
