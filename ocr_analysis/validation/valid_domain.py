import whois

def is_domain_valid(domain_name) -> bool:
    """
    Checks the validity of the given domain name (domain_name).

    Args:
    domain_name (str): The domain name to be checked for validity.

    Returns:
    bool: Returns True if the domain name is valid, False otherwise.

    If a Whois query is successfully completed and ownership information is available,
    the domain name is considered valid and returns True. Otherwise, it returns False.
    In case of any errors, the domain name is not considered valid and returns False.
    """
    try:
        domain_info = whois.whois(domain_name)
        
        if domain_info.status:
            return True
        else:
            return False
    except Exception as e:
        return False

