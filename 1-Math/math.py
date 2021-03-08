def approx(num: float, precision: int = 0) -> float:
    """
    Return the approximation of num to the nearest precision
    :param num: int | float
    :param precision: int
    :return: int | float
    """
    factor = 10 ** (precision + 1)
    factored_num = num * factor
    last_digit = factored_num % 10
    return (factored_num + 10 - last_digit)/factor if last_digit > 4 else (factored_num - last_digit)/factor


