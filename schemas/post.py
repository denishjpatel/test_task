from pydantic import BaseModel, constr

class PostCreate(BaseModel):
    text: constr(max_length=1000)  # Assuming 1MB ~ 1000 characters for simplicity

class PostResponse(BaseModel):
    id: int
    text: str