from fastapi import APIRouter
from .service import  get_Depression
from .schema import DepressionRequest


router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_Depression(data: DepressionRequest):
    return {"message":"natisa"}