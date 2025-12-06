def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# ---- Testing the function ----
print(is_prime(11))  # Expected: True
print(is_prime(15))  # Expected: False
print(is_prime(2))   # Expected: True
print(is_prime(1))   # Expected: False

