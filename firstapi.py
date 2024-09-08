from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def read_root(name: str):
    return {f"Message" : "Congrats {name}! This is your first API"}