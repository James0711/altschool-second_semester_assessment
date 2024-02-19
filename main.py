# import required libraries
from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

# A dictionary to store the student data
students = {}

student_data = {"id": 0, "Name": "", "age": 0, "sex": "", "height": 0.0}

@app.get("/")
def home():
    return {"message": "Welcome to AltSchool Student Database"}

#creating a student resource
@app.post("/students") # A POST method used in creating a student resource
def create_student(name: str, age: int, sex: str, height: float):

    new_student = student_data.copy()
    id = len(students) + 1
    uuid_id = str(UUID(int=id))
    new_student["id"] = uuid_id
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height 

    students[new_student["id"]] = new_student
    return {"message": "Student created successfully", "data": new_student}

# Get all (many) students
@app.get("/students")
def get_students():
    return {"message": "successful", "data": students}

# Get a single Student
@app.get("/students/{id}")
def get_student(id):
    student = students.get(id)
    if not student:
        return {"error": "student not found!"}
    
    return {"message": "successful", "data": student}

# Update a student
@app.put("/students/{id}") # A PUT method to update the student resource
def update_student(id: str, name: str, age: int, sex: str, height: float):
     student = students.get(id)

     if not student:
        return {"error": "student not found!"}
     
     student["name"] = name
     student["age"] = age
     student["sex"] = sex
     student["height"] = height

     return {"message": "student updated successfully", "data": student}

# Delete a student
@app.delete("/students/{id}") 
def delete_student(id: str):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}
    
    del students[id]
    return {"message": "student deleted successfully"}