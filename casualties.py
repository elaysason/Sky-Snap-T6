from fastapi import APIRouter, HTTPException
from pydantic import PositiveInt
from casualties_types import CasualtyData
from global_types import Side, Metric, MetricsDescription

router = APIRouter()

@router.get("/Casualties/")
def get_all_casualties():
    return casualties_data

@router.get("/Casualties/{casualty_id}")
def get_casualty_by_id(casualty_id: PositiveInt):
    casualty = next((c for c in casualties_data if c.casualty_id == casualty_id), None)
    if casualty is None:
        raise HTTPException(status_code=404, detail="Casualty not found")
    return {"casualty": casualty}

@router.get("/Casualties/{per_side}")
def get_casualties_by_side(per_side: Side):
    # get red val from lea
    # get blue val from lea
    return {
        Side.Red: Metric(
            description=MetricsDescription.CasualtiesCount,
            value=1,
            ),
        Side.Blue: Metric(
            description=MetricsDescription.CasualtiesCount,
            value=1
            ),
        }