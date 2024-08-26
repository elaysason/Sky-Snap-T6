from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import NonNegativeInt
from .casualties_types import CasualtyData, SidedCasualities
from global_types import Metric, MetricsDescription


router = APIRouter()

@router.get("/casualties")
def get_all_casualties() -> List[CasualtyData]:
    return casualties_data

@router.get("/casualties/{casualty_id}")
def get_casualty_by_id(casualty_id: NonNegativeInt) -> CasualtyData:
    casualty = next((c for c in casualties_data if c.casualty_id == casualty_id), None)
    if casualty is None:
        raise HTTPException(status_code=404, detail="Casualty not found")
    return CasualtyData()

@router.get("/casualties/per_side")
def get_casualties_by_side() -> SidedCasualities:
    # get red val from lea
    # get blue val from lea
    return SidedCasualities(
        כחול=Metric(
            description=MetricsDescription.CasualtiesCount,
            value=1,
            ),
        אדום=Metric(
            description=MetricsDescription.CasualtiesCount,
            value=1
            ),
        )