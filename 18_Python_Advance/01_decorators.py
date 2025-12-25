# decorator is a function that takes  a function, it creates a new func inside it's body (wrapper) and returns new function.

#1st way of writing decorator
# def decorator(func):  
#   def wrapper():
#     print("Before executing the function")
#     func()
#     print("After executing the function")
#   return wrapper

# def say_hello():
#   print("Hello, World!")

# f = decorator(say_hello) 
# f()  

#2nd way of writing decorator 
def decorator(func):  
  def wrapper():
    print("Before executing the function")
    func()
    print("After executing the function")
  return wrapper
@decorator

def say_hello():
  print("Hello, World!")
say_hello()  
