from fastapi import FastAPI
from launches.launches import router as launches_router  # Import the router from launches.py
from casualties.casualties import router as casualties_router  # Import the router from launches.py
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed origins
    allow_credentials=True,  # Whether or not to allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # Allowed HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allowed HTTP headers
)

app.include_router(launches_router)
app.include_router(casualties_router)
