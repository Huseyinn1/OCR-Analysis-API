
import re
from ocr_analysis.validation.valid_credit_card import luhn_algorithm
from ocr_analysis.validation.valid_email import verify_email
from ocr_analysis.validation.valid_url import validate_url
from ocr_analysis.validation.valid_domain import is_domain_valid
from ocr_analysis.validation.valid_id import validate_tc_kimlik_no
from ocr_analysis.validation.valid_plate import is_valid_plate_number
from ocr_analysis.validation.valid_hash import identify_hash_algorithms
from ocr_analysis.validation.valid_phone_number import validate_turkish_phone_number
from ocr_analysis.config import DATA_PATTERN

def get_extract_data(checked_text) -> list:
    """
    A function that extracts data matching specific patterns from a text.

    param -> checked_text: The text from which data will be extracted.

    type -> checked_text: str

    return -> A list containing data matching specific patterns.
    """
    findings = []
    for data_type, pattern in DATA_PATTERN.items():
        matches = re.findall(pattern, checked_text)
        for match in matches:
            findings.append({"value": match, "type": data_type})
    return findings


validation_functions = {
    "PHONE_NUMBER":validate_turkish_phone_number,
    "CREDIT_CARD_NUMBER": luhn_algorithm,
    "EMAIL": verify_email,
    "URL": validate_url,
    "DOMAIN": is_domain_valid,
    "ID_NUMBER": validate_tc_kimlik_no,
    "PLATE": is_valid_plate_number,
    "HASH": identify_hash_algorithms
 
}
def get_extract_findings(finding) -> dict:
    """
    Validates a given finding and sets the 'is_valid' field if it is valid.

    Args:
        finding (dict): A dictionary representing the finding. The dictionary should include "type" and "value" fields.

    Returns:
        dict: The finding dictionary with the 'is_valid' field added if it is valid.
    """
    is_valid = None
    
    validation_function = validation_functions.get(finding["type"])
    if validation_function:
        is_valid = validation_function(finding["value"])
    
    if is_valid is not None:
        finding["is_valid"] = is_valid
    
    return finding