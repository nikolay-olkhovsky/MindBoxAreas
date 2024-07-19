from inspect import getmembers, isfunction
import figure

def area(*args, type):
    if len(args) < 1:
        raise ValueError("No arguments to compute area of \'{0}\'".format(type))
    functions = dict(getmembers(figure, isfunction))
    if type in functions.keys():
        return functions[type](*args)
    else:
        raise ValueError("The area for type \'{0}\' is not implemented.".format(type))
