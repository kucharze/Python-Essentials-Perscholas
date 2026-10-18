def validate_age(age):
    """
    Validates the given age.

    Parameters:
    age (int): The age to validate.

    Returns:
    bool: True if the age is valid, False otherwise.
    """
    if isinstance(age, int) and 0 <= age <= 120:
        return True
    
    raise ValueError("Age must be an integer between 0 and 120.")
    
    return False