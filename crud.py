from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

myapp = FastAPI()

# Student model
class Student(BaseModel):
    id: int
    name: str
    age: int
    bloodgroup: str

# In-memory list to store students
students: List[Student] = []

# Create student
@myapp.post("/students", response_model=Student)
async def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    students.append(student)
    return student

# Get all students
@myapp.get("/students", response_model=List[Student])
async def get_students():
    return students

# Update student
@myapp.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, updated_student: Student):
    for index, s in enumerate(students):
        if s.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

# Delete student
@myapp.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for index, s in enumerate(students):
        if s.id == student_id:
            students.pop(index)
            return {"detail": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
