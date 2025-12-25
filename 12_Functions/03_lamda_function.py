# A lambda function is a small, anonymous (nameless) function in Python.It’s used for short, one-line operations where defining a full def function would be unnecessary.

# Normal function
def add(x, y):
    return x + y

# Same thing using lambda
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))


square= lambda a: a*a
print(square(5))