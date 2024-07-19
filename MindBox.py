import sys
from areas import triangleArea, circleArea

_in = list(map(float, sys.argv[1:]))

if len(_in) == 3:
    _out = triangleArea(_in[0], _in[1], _in[2])
    print("This is a triangle!\nArea: {0}.".format(_out))
elif len(_in) == 1:
    _out = circleArea(_in[0])
    print("This is a circle!\nArea: {0}.".format(_out))
