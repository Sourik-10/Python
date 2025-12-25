def fibonacci(n):
    '''
    Print the first n Fibonacci numbers using recursion.
    '''
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    for i in range(n):
        print(fib(i), end=" ")

fibonacci(10)  
