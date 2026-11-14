from pydantic import BaseModel
from fastapi import FastAPI, status


app=FastAPI()

class Student(BaseModel):
    name: str
    age: int
    hue: str | None = None

class StudentResponse(BaseModel):
    name: str
    age: int
    hue: str | None = None
    
@app.post("/student", response_model=Student, status_code=status.HTTP_201_CREATED)
def student(student: Student):
    st = StudentResponse(name=student.name, age=student.age, hue="hue")
    return {
        "name": student.name, "age":student.age
    }