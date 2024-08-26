import datetime
from pydantic import BaseModel, Field

class LaunchData(BaseModel):
    launch_id: int
    casualty_id: int
    type_id: int
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

class rocket_type_data(BaseModel):
    name_he: str
    metric1: Metric 
    metric2: Metric 
    metric3: Metric

