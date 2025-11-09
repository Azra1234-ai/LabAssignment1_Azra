# LabAssignment1_Azra
[is_prime().py](https://github.com/user-attachments/files/23440439/is_prime.py)
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

[reverse_string().py](https://github.com/user-attachments/files/23440450/reverse_string.py)
def reverse_string(s: str) -> str:
    """Return a new string that is the reverse of the input string."""
    return s[::-1]

if __name__ == "__main__":
# ---- Testing the function ----
    print(reverse_string("hello"))
    print(reverse_string("Python"))
    print(reverse_string("Github"))

    [recursive_iterative().py](https://github.com/user-attachments/files/23440454/recursive_iterative.py)
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

[largest_number().py](https://github.com/user-attachments/files/23440457/largest_number.py)
def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

# Example usage
numbers = [3, 5, 7, 2, 8]
print("The largest number is:", find_largest_number(numbers))
if __name__ == "__main__":
    # ---- Testing the function ----
    print(find_largest_number([1, 2, 3, 4, 5]))  # Expected: 5
    print(find_largest_number([-10, -20, -5, -15]))  # Expected: -5
    print(find_largest_number([42]))  # Expected: 42
    
[Lab_Assignment_1(Azra).docx](https://github.com/user-attachments/file[README.md](https://github.com/user-attachments/files/23440471/README.md)
s/23440463/Lab_A# LabAssignment1_Azra
ssignment_1.Azra.docx)

