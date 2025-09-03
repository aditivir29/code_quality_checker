# sample.py

# Simple correct function
def add_numbers(a, b):
    return a + b

# Function with PEP8 violations (extra spaces, missing space)
def multiply_numbers(a ,b):
  return a*b

# Function with syntax error (missing colon)
def divide_numbers(a, b)
    if b != 0:
        return a / b
    else:
        return None

# Function with logical error
def subtract_numbers(a, b):
    result = a + b  # Should be a - b
    return result

# Function with higher complexity
def complex_function(x):
    if x > 0:
        if x % 2 == 0:
            print("Positive even")
        else:
            print("Positive odd")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
