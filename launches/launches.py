from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException
from .launches_service import (
    get_launch_by_id,
    get_launches, 
    get_launches_by_date_range,
    get_launches_by_type,
    )
from .launches_types import LaunchData


router = APIRouter()

@router.get("/launches")
async def read_launches():
    return get_launches()

@router.get("/launches/{id}" )
async def read_launch(id: int):
    launch = get_launch_by_id(id)
    if launch is None:
        raise HTTPException(status_code=404, detail="Launch not found")
    return launch

@router.get("/launches/type/{type}", response_model=List[LaunchData])
async def read_launches_by_rocket_type(type: int):
    return get_launches_by_type(type)


@router.get("/launches/date_range/{start_date}/{end_date}", response_model=List[LaunchData])
async def read_launches_by_date_range(start_date: str, end_date: str):
    try:
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format, please use YYYY-MM-DD HH:MM:SS")
    
    return get_launches_by_date_range(start_date_dt, end_date_dt)


