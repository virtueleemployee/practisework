from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()                      


class student(BaseModel):
    name:str
    age:int
    place:int

@app.post("/students")
def see(suzi:student):
    return {"message":"hello {suzi.name} are u from {suzi.place}"}
    