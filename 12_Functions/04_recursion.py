# Recursion means a function calling itself until a certain condition (base case) is met.It’s often used for tasks that can be broken into smaller, similar sub-tasks (like factorial, Fibonacci, etc.).

#                 fib(5)
#               /        \
#          fib(4)          fib(3)
#         /     \          /     \
#     fib(3)   fib(2)   fib(2)   fib(1)
#     /   \    /   \    /   \
# fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
#  / \
# fib(1) fib(0)

def fib(n):
    if n <= 1:   # base case
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5)) 


def factorial(n):
    if n == 0 or n == 1: # base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
