def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# ---- Testing the function ----
print(factorial(5))  # Expected: 120
print(factorial(0))  # Expected: 1
