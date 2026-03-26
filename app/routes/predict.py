from fastapi import APIRouter
from app.services.model_service import predict_image

router = APIRouter()

@router.get("/predict")
def predict():
    return predict_image()