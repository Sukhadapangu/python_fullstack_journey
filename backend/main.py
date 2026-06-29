from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class User(BaseModel):
    user_id: int
    username: str
    email: str
    is_active: bool = True
    tags: List[str] = []
    phone_number: Optional[str] = None
    role: str = "viewer"


@app.post("/users/")
async def create_user(user: User):

    print(f"Received user: {user.username}")

    return {"message": "User created successfully!", "user_data": user}
