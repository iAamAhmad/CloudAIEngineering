from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
   return {"Hello"}
@app.get("/home")
def ahmad():
   return {"Hello,where have you been so far?"}
@app.get("/about")
def ahmad():
   return {"Hello,where have you been so far? tell me something about You!!!"}
