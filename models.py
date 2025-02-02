from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "make"
    female = "female"
    other = "other"

class role(str, Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email: str
    role: list[role]