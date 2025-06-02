'''
Hayden Hartmann
Coding Problem: Solve Fibonacci Series problem using recursion
6/1/2025
'''
# this function finds the n'th fibonacci number, which is a sum of the previous two numbers
def FibonacciNumber(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciNumber(n - 1) + FibonacciNumber(n - 2)

print(FibonacciNumber(5))





