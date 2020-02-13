from datetime import date

__all__ = ['isInt', 'isFloat', 'isDate']


def isInt(value):
    """
    Determine if the string value can be parsed into int
    Args:
        value(int): String value
    Returns:
        True/False
    """
    try:
        if (
            value.lstrip("+-")
        ).isnumeric():
            return True
        else:
            return False
    except Exception as e:
        del e
        return False


def isFloat(value):
    """
    Determine if the string value can be parsed into float
    Args:
        value(int): String value
    Returns:
        True/False
    """
    try:
        if float(value):
            return True
        else:
            return False
    except Exception as e:
        del e
        return False


def isDate(value):
    """
    Determine if the string value can be parsed into date
    Args:
        value(int): String value
    Returns:
        True/False
    """
    try:
        if date.fromisoformat(value):
            return True
        else:
            return False
    except Exception as e:
        del e
        return False
