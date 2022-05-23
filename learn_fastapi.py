from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    year:Optional[str] = None


#Creating a student just to have something to play with.
students={
    1: Student(name='john',age=17,year='year 12')
}

#Base function to appear on the page, just to make sure it works.
@app.get('/')
def index():
    return {"name":"First Data"}

#get a student by student_id.
@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path(None, description= "The ID of the student you want to view")):
    return students[student_id]

#get a student by its name.
@app.get('/get-by-name/{student_id}')
def get_student(*,student_id: int, name: Optional[str] =None,test:int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data":"Not found"}

print ('Done')

#create a student.
@app.post('/create-student/{student_id}')
def create_student(student_id: int,student:Student):
    if(student_id in students):
        return {"Error":"Student exists"}
    
    students[student_id]=student
    return students[student_id]

#Update certain values on an existing student.
@app.put('/update-student/{student_id}')
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student doesn't exist"}
    updatedStudent={}
    for key,value in students[student_id]:
        print (key,value)
        if (student.dict()[key]!=None):
            updatedStudent[key]=student.dict()[key]
        else:
            updatedStudent[key]=students[student_id].dict()[key]
    students[student_id]=Student(**updatedStudent)
    return students[student_id]

    
            

