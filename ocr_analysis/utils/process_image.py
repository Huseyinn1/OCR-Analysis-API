
from fastapi import  UploadFile,HTTPException
from fastapi.responses import JSONResponse
from ocr_analysis.utils.get_extract_data import get_extract_data,get_extract_findings
from ocr_analysis.cache.cache_manager import get_cached_result,cache_result
from PIL import Image
import pytesseract
import io
import json

def process_image(image: UploadFile) -> dict:
    """
    Processes the provided uploaded image file, extracts text, and analyzes the findings.

    Args:
        image (UploadFile): The uploaded image file.

    Returns:
        JSONResponse: A JSON response containing the processed text, processing status, and extracted findings.

    Raises:
        HTTPException: May raise HTTP request errors if the image cannot be read or content cannot be found.
    """
    image_data = image.file.read()
    
    cached_result = get_cached_result (image_data)
    
    if cached_result:
        cached_results = json.loads(cached_result)
        return JSONResponse(content=cached_results)
    
    try:
        image = Image.open(io.BytesIO(image_data))

    except Exception:
        raise HTTPException(status_code=400, detail="Image could not be read. Invalid format.")
    
    checked_text = pytesseract.image_to_string(image)
    checked_text = checked_text.replace("\n", " ")
    
    if not checked_text.strip():
         raise HTTPException(status_code=204,detail="Image read but content not found")

    findings = get_extract_data(checked_text)
    processed_findings = [get_extract_findings(finding) for finding in findings]
    
    response = {
        "content": checked_text,
        "status": "successful",
        "findings": processed_findings,
    }
    cache_result(image_data,json.dumps(response))

    return JSONResponse(content=response)

