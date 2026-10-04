# Practical 1: Fibonacci Numbers

# Non-Recursive Fibonacci
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = fibonacci_recursive(n - 1)
    fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


# Driver Code
n = int(input("Enter total numbers to print in Fibonacci series: "))
print("Fibonacci Series (Non-Recursive):", fibonacci(n))
print("Fibonacci Series (Recursive):    ", fibonacci_recursive(n))
