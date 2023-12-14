
import math

def transform(num: float) -> float:
    """
    Return the square root of the 100 times of the given number

    If the num is negative, returns 0.
    """
    if num < 0:
        return 0
    return math.sqrt(num * 100)

