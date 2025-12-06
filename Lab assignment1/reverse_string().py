def reverse_string(s: str) -> str:
    """Return a new string that is the reverse of the input string."""
    return s[::-1]

if __name__ == "__main__":
# ---- Testing the function ----
    print(reverse_string("hello"))
    print(reverse_string("Python"))
    print(reverse_string("Github"))