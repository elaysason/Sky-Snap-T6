from fastapi import FastAPI
from launches.launches import router as launches_router  # Import the router from launches.py
from casualties.casualties import router as casualties_router  # Import the router from launches.py


app = FastAPI()

app.include_router(launches_router)
app.include_router(casualties_router)
