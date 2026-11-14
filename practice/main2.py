from fastapi import FastAPI

app = FastAPI(title = "fast api", description="hue hue", version="1.0.0")


student = ["Shivam", "Pathak", "Gunjan", "Nikhade"]

@app.get("/getStudent/{student_id}")
def getStudent(student_id: int):
    return {"student": student[student_id]} 


@app.get("/getStudent")
def studentInfo(name: str, age: int):
    return {"name" : f"Name is {name} and age is {age}"}
