from fastapi import FastAPI                         
from pydantic import BaseModel                


app =FastAPI()                          #the function that says like it will handles the request


# its just a first API
@app.get("/hello")

def read_hello():
    return{"message": "hello world im new to this  office"}

@app.get("/namasthe")

def read_namasthe():
    return{"message":"namasthe sagar and mohit bro"}

@app.get("/student")

def read_student():
    return{"message":"all students are passed in the examination"}


#   PATH PARAMETER

@app.get("/hello/{name}")                    

def greet_name(name:str):
    return{"message":"hello {sagar}"}


@app.get("/hallo/{num}")

def greet_num(num :int):
    return{"message":f" hello {num}"}


@app.get("/hello/{num1}")

def greet_num(num:int):
    return{"message":f"hello {8055}"}



# QUERY PARAMETER

fruits_list =["apple","bannana","mango","kiwi","grapes","Honeydew", "Iceberg Lettuce", "Jackfruit"]

@app.get("/items")

def reading(skip: int =0,limit:int = 4):
    return{"items":fruits_list[skip:skip + limit]}

list =[2,3,4,5,6,7,8,9,5,63,0]

@app.get("/numbers")

def collect(skip:int =5,limit:int =7):
    return{"lists":list[skip:skip+limit]}


class Details(BaseModel):  
    name: str
    age: int
    place: str

@app.post("/details")
def creating_detail(detail: Details):  
    return detail


#response model

class item(BaseModel):
    name:str
    price:float

@app.post("/items")

def create_item(it:item):
    return it


class itemresponse(BaseModel):
    name:str
    clr:str
    price:float

@app.post("/vegetables:response_model = itemresponse")
def vege(this:item):
    return item    


#serialization

class users(BaseModel):
    name:str
    id:int

@app.post("/user",response_model = users)
async def showing(userr:users):
    user = user(name ="karthik",id =2211)
    return userr


class users(BaseModel):
    name:str
    id:int

@app.get("/user",response_model = users)
async def showing():
    user = user(name ="karthik",id =2211)
    return users
    



 #   CRUD OPERATION   (BEFORE USING DATABASE I USING LIST IT ACT AS A DB)

class items(BaseModel):
    id :int
    name:str
    price:float

@app.post("/list",response_model = items)

async def showlist(item:items):
    return item 






