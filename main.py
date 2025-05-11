from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str

@app.post("/greet")
async def greet_user(data: InputData):
    return {"message": f"Hello, {data.name}!"}
