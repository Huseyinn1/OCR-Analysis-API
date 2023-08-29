
from fastapi import UploadFile, File,APIRouter
from ocr_analysis.utils.process_image import process_image

router = APIRouter()


@router.post("/analyze_image/")
async def analyze_image(image: UploadFile = File(...)):
    result = process_image(image)
    return result
