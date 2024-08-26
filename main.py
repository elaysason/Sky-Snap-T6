from fastapi import FastAPI
from launches import router as launches_router  # Import the router from launches.py


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(launches_router)