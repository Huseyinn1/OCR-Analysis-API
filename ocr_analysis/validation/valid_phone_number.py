import phonenumbers

def validate_turkish_phone_number(phone_number) -> bool:
    """
    Checks whether the given phone number (phone_number) conforms to the Turkish format.

    Args:
    phone_number (str): The phone number to be checked.

    Returns:
    bool: Returns True if the phone number conforms to the Turkish format, otherwise False.
    """
    try:
        parsed_number = phonenumbers.parse(phone_number, "TR")
        if phonenumbers.is_valid_number(parsed_number):
            return True
        else:
            return False
    except phonenumbers.phonenumberutil.NumberFormatException:
        return False
