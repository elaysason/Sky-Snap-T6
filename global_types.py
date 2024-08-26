from pydantic import NonNegativeFloat, BaseModel
from enum import Enum


class MetricsDescription(Enum):
    CasualtiesCount = "כמות נפגעים"
    LaunchesCount = "כמות שיגורים"
    Time = "זמן"
    Distance = "מרחק"
    Interception = "יורט/לא יורט"

class Metric(BaseModel):
    value: NonNegativeFloat
    description: MetricsDescription