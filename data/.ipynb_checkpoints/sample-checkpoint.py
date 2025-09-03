# sample.py

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return None

def complex_function(x):
    if x > 0:
        if x % 2 == 0:
            print("Positive even")
        else:
            print("Positive odd")
    else:
        print("Non-positive")
