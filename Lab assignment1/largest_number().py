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
