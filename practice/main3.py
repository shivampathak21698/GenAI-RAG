from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI

app=FastAPI()

class Subject(BaseModel):
    sub1: str
    sub2: str

class Student(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    name: str
    age: int
    subject: Subject

# student = Student(name="Shivam Pathak", age=29,  subject=Subject(sub1="Hindi", sub2="English"))

# student.name = "Hue"
# print(student)


@app.post("/student")
def student(student: Student):
    return {"request is": student}