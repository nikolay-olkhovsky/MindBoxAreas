import math

def circleArea(r):
    return math.pi * r ** 2

def triangleArea(a, b, c):
    if a > b:
        if a > c and a**2 == b**2 + c**2:
            return (b * c) / 2.
        elif c**2 == a**2 + b**2:
            return (a * b) / 2.
    elif b > c and b**2 == a**2 + c**2:
        return (a * c) / 2.
    elif c**2 == a**2 + b**2:
        return (a * b) / 2.
    p = (a + b + c) / 2.
    res = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return res
