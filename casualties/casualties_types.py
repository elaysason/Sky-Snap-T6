from pydantic import BaseModel, NonNegativeInt
from global_types import Metric


class CasualtyData(BaseModel):
    casualty_id: NonNegativeInt
    mortal_injured: NonNegativeInt
    hard_injured: NonNegativeInt
    medium_injured: NonNegativeInt
    easy_injured: NonNegativeInt
    death_count: NonNegativeInt


class SidedCasualities(BaseModel):
    כחול: Metric
    אדום: Metric
