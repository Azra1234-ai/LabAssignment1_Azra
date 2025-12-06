def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# ---- Testing the functions ----
print(recursive_factorial(5))  # Expected: 120
print(iterative_factorial(5))  # Expected: 120