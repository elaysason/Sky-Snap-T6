import datetime
from typing import List
from fastapi import APIRouter

from .launches_types import LaunchData

router = APIRouter()

@router.get("/launches", response_model=List[LaunchData])
async def read_launches():
    return {"message": "This is the launches endpoint"}

@router.get("/launches/{launch_id}", response_model=LaunchData)
async def read_launch(launch_id: int):
    return LaunchData(id=launch_id, name=f"Launch {launch_id}", description="A detailed description of the launch.")

@router.get("/launches/rocket_type/{rocket_type}", response_model=List[LaunchData])
async def read_launches_by_rocket_type(rocket_type: int):
    return {"message": f"This is the launches endpoint for rocket type {rocket_type}"}

@router.get("/launches/date_range/{start_date}/{end_date}", response_model=List[LaunchData])
async def read_launches_by_date_range(start_date: str, end_date: str):
    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
    
    filtered_launches = []
    return filtered_launches


