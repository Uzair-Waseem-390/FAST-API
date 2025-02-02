from fastapi import FastAPI
from typing import List
from uuid import uuid4, UUID
from models import User, role, Gender
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        first_name="Uzair",
        last_name="Waseem",
        middle_name="",  
        email="uzairwaseem@gmail.com",
        role=[role.admin],
        gender = Gender.male,
        ),
    User(
        id=UUID("87654321-4321-8765-4321-876543218765"),
        first_name="Hassan Mehmood",
        last_name="Mehmood",
        middle_name="",
        email="hassan@gmail.com",
        role=[role.teacher],
        gender = Gender.male,
        ),
    User(
        id=UUID("87654321-4321-8765-4321-876543218678"),
        first_name="Moaze",
        last_name="Waseem",
        middle_name="",
        email="moazewaseem@gmail.com",
        role=[role.teacher],
        gender = Gender.male,
        ),

]

@app.get("/")
def root():
    return {"message": "Uzair is a good Boy"}
@app.get("/api/users")
async def get_users():
    return db
@app.post("/api/users")
async def create_user(user: User):
    print("User added", user)
    db.append(user)
    return user
@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User Deleted"}
    return {"message": "User Not Found"}














# @app.get("/uzair")
# def uzair():
#     return {"message": "Uzair is Using Fast API"}
# @app.get("/uzair/ai")
# def uzair():    
#     print("function call")
#     return {"message": "Learning AI"}  
# @app.post("/uzair/rquest")
# def uzair():
#     print("function call")
#     return {"message": "Any Request Send to backend"}      
# @app.put("/uzair/ok")
# def uzair():
#     print("function call")
#     return {"message": "Data Updated"}