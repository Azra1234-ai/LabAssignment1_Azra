[is_prime().py](https://github.com/user-attachments/files/23440550/is_prime.py)# LabAssignment1_Azra
[Uploadingdef is_prime(n):
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

 is_prime().py…]()

