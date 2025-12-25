# Positional Arguments
def add(a, b):
    return a + b

print(add(10, 5))  

# Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Default value "Guest" 
print(greet("Sourik"))  # "Sourik" override

# keyword Arguments
def add(a, b):
    return a - b

print(add(b=2,a=4 ))  