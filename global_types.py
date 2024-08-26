from pydantic import NonNegativeFloat, BaseModel
from enum import Enum

class Side(Enum):
    Blue = "כחול"
    Red = "אדום"

class MetricsDescription(Enum):
    CasualtiesCount = "כמות נפגעים"
    LaunchesCount = "כמות שיגורים"
    Time = "זמן"
    Distance = "מרחק"
    Interception = "יורט/לא יורט"

class Metric(BaseModel):
    value: NonNegativeFloat
    description: MetricsDescription