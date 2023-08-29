import httpx
from ocr_analysis.config import settings



def verify_email(email: str) -> bool:
    """
    Verifies the accuracy of the given email address.

    Args:
    email (str): The email address to be verified.

    Returns:
    bool: Returns True if the email address can be verified, otherwise False.

    This function uses the emailable.com API to validate the given email address.
    The process involves sending an HTTP GET request to the API to validate the email address and checking the result.
    If the email address can be verified (state='deliverable'), it returns True; otherwise, it returns False.
    In case of any HTTP errors, it returns False and prints the error.

    Notes:
    - For this function to work correctly, the EMAILABLE_API_KEY variable must be set correctly.
    - In case of an error during the HTTP request, the function returns False and prints the error.
    """

    api_url = f"https://api.emailable.com/v1/verify"
    params = {"email": email, "api_key": settings.EMAILABLE_API_KEY}

    with httpx.Client() as client:
        try:
            response = client.get(api_url, params=params)
            response.raise_for_status()
            verification_result = response.json()
            is_deliverable = verification_result.get('state') == 'deliverable'
            return is_deliverable
        
        except httpx.HTTPError as e:
            print("Error:", e)
            return False
