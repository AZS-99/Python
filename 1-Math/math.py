def approx(num: float, precision: int = 0) -> float:
    factor = 10 ** (precision + 1)
    factored_num = num * factor
    last_digit = factored_num % 10
    return (factored_num + 10 - last_digit)/factor if last_digit > 4 else (factored_num - last_digit)/factor


def factorial(num: int) -> int:
    return 1 if num == 1 else factorial(num - 1) * num


def gcd(num1: int, num2: int) -> int:
    if num1 < num2:
        num1, num2 = num2, num1
    return num2 if num1 % num2 == 0 else gcd(num2, num1 % num2)


def sum_digits(num: int) -> int:
    if num < 10:
        return num
    return num % 10 + sum_digits(num // 10)
