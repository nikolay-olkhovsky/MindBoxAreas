import math

def circle(*args):
    if len(args) != 1:
        raise ValueError("Wrong number of parameters for circle ({0})".format(len(args)))
    r = args[0]
    if r < 0. : 
        raise ValueError("Radius r cannot be < 0. (current value {0})".format(r))
    return math.pi * r ** 2

def triangle(*args):
    if len(args) != 3:
        raise ValueError("Wrong number of parameters for triangle ({0})".format(len(args)))
    a = args[0]
    b = args[1]
    c = args[2]
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("A triangle side cannot be <= 0. (current values a={0}, b={1}, c={2})".format(a, b, c))
    if a >= b+c or b >= a+c or c >= a+b:
        raise ValueError("A triangle side cannot be greater or equal to the sum of other sides (current values a={0}, b={1}, c={2})".format(a, b, c))
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
