def convert_to_celsius (fahrenheit):
    """(number) -> float

    Return the number of Celisus degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius (75)
    23.8888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0

def adove_freezing(celsius):
    """ (number) -> bool

    Return True iff temperature   celsius degrees is adove freezing.

    >>> adove_freezing(5.2)
    True
    >>> adove_freezing(-2)
    False
    """

    return celsius > 0
