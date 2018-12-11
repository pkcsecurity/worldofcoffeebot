import math


def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    return obj.__dict__


def distance(p1, p2):
    a1, b1 = p1
    a2, b2 = p2

    a = abs(a2 - a1)
    b = abs(b2 - b1)

    return math.sqrt(a ** 2 + b ** 2)
