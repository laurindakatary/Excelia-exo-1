import random


def generate_cookie_value():
    """
    >>> len(generate_cookie_value())
    128
    """

    return str("".join(random.choice("0123456789ABCDEFabcdef@&!") for i in range(128)))


def somme(a, b):

    # doctest debut
    """
    >>> somme(2,4)
    {'Result': 6}
    """

    y = int(a) + int(b)
    return {"Result": y}
