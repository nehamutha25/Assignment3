# Task 1: Calculate factorial using a function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample function call
number = 5
print(f"The factorial of {number} is:", factorial(number))
