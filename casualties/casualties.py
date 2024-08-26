from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import NonNegativeInt

from casualties.casualties_service import casualties, casualty_by_id
from .casualties_types import CasualtyData, SidedCasualities
from global_types import Metric, MetricsDescription


router = APIRouter()

@router.get("/casualties")
def get_all_casualties() -> List[CasualtyData]:
    return casualties()

@router.get("/casualties/{casualty_id}")
def get_casualty_by_id(casualty_id: NonNegativeInt) -> CasualtyData:
    casualty = casualty_by_id(casualty_id)
    if casualty is None:
        raise HTTPException(status_code=404, detail="Casualty not found")
    return casualty

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