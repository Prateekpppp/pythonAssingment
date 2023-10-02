def fibonacci_series(n):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

fibonacci_series_50 = fibonacci_series(50)
print(fibonacci_series_50)