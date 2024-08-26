import datetime
from pydantic import BaseModel, Field, NonNegativeInt
from global_types import Metric


class LaunchData(BaseModel):
    launch_id: NonNegativeInt
    casualty_id: NonNegativeInt
    type_id: NonNegativeInt
    is_red_side: bool
    start_date: datetime.datetime
    end_date: datetime.datetime
    start_location_x: float
    start_location_y: float
    end_location_x: float
    end_location_y: float
    was_intercepted: bool
    rocket_type: int = Field(ge=1, le=3)  # Ensure rocket_type is within the specified range
    time: datetime.timedelta  # Assuming timedelta represents a duration
    speed: float
    distance: float


class RocketTypeData(BaseModel):
    name_he: str
    metric1: Metric 
    metric2: Metric 
    metric3: Metric
