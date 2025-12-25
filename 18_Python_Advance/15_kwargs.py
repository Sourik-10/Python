def marks(**kwargs):
    # **kwargs is a dictionary containing all key-value pairs passed to the function
    for subject in kwargs.keys():
        print(kwargs[subject])

marks(math=85, english=90, science=88)

