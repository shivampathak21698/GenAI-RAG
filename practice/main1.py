from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def getInfo():
    return {"message" : "Hello From Python FastAPI Example"}

@app.get("/student")
def getStudent():
    return [{"name": "Rex", "age":"28"}, {"name": "Rex", "age":"28"}, {"name": "Rex", "age":"20"}, {"ice-cream"}]


@app.post("/students")
def getStudent():
    return "hue"



