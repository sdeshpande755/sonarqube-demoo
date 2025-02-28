def add(a, b):
    return a + b

def subtract(a, b):  # Untested function
    return a - b

def multiply(a, b):  # Untested function
    return a * b

def divide(a, b):  # Untested function
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# ✅ Only one function has a test (low coverage)
if __name__ == "__main__":
    print(add(2, 3))  # Only this function is tested
