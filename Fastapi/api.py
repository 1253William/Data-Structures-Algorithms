from fastapi import FastAPI, Path

#Instance
app = FastAPI()

#data
students = {
    1: {
        "name": "John",
        "age": "16",
        "class": "year 12"
    },
    2: {
        "name": "Ensam",
        "age": "16",
        "class": "year 12"
    },
    3: {
        "name": "Jule",
        "age": "16",
        "class": "year 12"
    },
    4: {
        "name": "Kev",
        "age": "16",
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"message": "Hello World"}

#path param
@app.get("/students/:id")
def student(student_id: int = Path(None, description="The ID of student you want to view", gt=0, lt=3)):
    return students[student_id]

#query param