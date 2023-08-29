

def luhn_algorithm(card_number)-> bool:
    """
    Checks the validity of the given credit card number using the Luhn algorithm.

    Args:
    card_number (int): The credit card number to be checked for validity.

    Returns:
    bool: Returns True if the card number is valid, False otherwise.

    The Luhn Algorithm is used to validate credit card numbers. This function verifies whether the given card number complies with the Luhn algorithm. The algorithm checks the last digit of the card to confirm that the card number has been calculated correctly.
    """
    
    
    digits = [int(digit) for digit in str(card_number)][::-1]

    odd_digits = digits[::2]
    even_digits = digits[1::2]

    even_digits = [2 * digit if digit < 5 else 2 * digit - 9 for digit in even_digits]

    total = sum(odd_digits + even_digits)

    return total % 10 == 0

