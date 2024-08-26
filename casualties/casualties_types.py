from pydantic import BaseModel, NonNegativeInt

class CasualtyData(BaseModel):
    casualty_id: NonNegativeInt
    mortal_injured: NonNegativeInt
    hard_injured: NonNegativeInt
    medium_injured: NonNegativeInt
    easy_injured: NonNegativeInt
    death_count: NonNegativeInt
