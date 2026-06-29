from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List
from datetime import datetime
from uuid import UUID, uuid4

app = FastAPI()


# ---------------- Address ----------------
class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., min_length=5, max_length=10)


# ---------------- Phone ----------------
class PhoneNumber(BaseModel):
    type: str = Field(..., pattern=r"^(home|work|mobile)$")
    number: str = Field(..., pattern=r"^\d{3}-\d{3}-\d{4}$")


# ---------------- User ----------------
class UserProfile(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    address: Address
    phone_numbers: List[PhoneNumber] = Field(default_factory=list)
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v


# ---------------- API ----------------
@app.post("/users/")
def create_user(user: UserProfile):
    return {"message": "User created successfully", "user": user}
