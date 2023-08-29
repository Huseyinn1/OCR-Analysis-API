


def validate_tc_kimlik_no(tc_kimlik_no) -> bool:
    """
    Checks the validity of the given Turkish Identification Number (tc_kimlik_no).

    Args:
    tc_kimlik_no (str): The Turkish Identification Number to be checked.

    Returns:
    bool: Returns True if the Turkish Identification Number is valid, otherwise False.
    """
    
    if len(tc_kimlik_no) != 11:
        return False

 
    if tc_kimlik_no[0] == '0':
        return False


    if not tc_kimlik_no.isdigit():
        return False

    
    toplam = sum(int(tc_kimlik_no[i]) for i in range(10))

   
    if toplam % 10 != int(tc_kimlik_no[10]):
        return False

    toplam2 = sum(int(tc_kimlik_no[i]) for i in range(0, 9, 2)) * 7
    toplam2 -= sum(int(tc_kimlik_no[i]) for i in range(1, 8, 2))

    if toplam2 % 10 != int(tc_kimlik_no[9]):
        return False

    return True
