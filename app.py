from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()                      

class Details(BaseModel):  
    name: str
    age: int
    place: str

@app.post("/details")
def creating_detail(detail: Details):  
    return{"message":"welcome ,{detail.name} from {detail.place}"}



    