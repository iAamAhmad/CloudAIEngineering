from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello"}

@app.get("/home/")
def ahmad():
    return {"message": "Hello, where have you been so far?"}

@app.get("/about/")
def khan():
    return {"message": "Hello, where have you been so far? Tell me something about You!!!"}
