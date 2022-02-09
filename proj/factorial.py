from proj.invalid_argument_error import InvalidArgumentError


def get_factorial(n):
    """Factorial function"""
    if isinstance(n, int) and n >= 0:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial
    else:
        raise InvalidArgumentError("Invalid argument. Integer greater than or equal to zero expected!")
