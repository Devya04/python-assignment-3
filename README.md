# python-assignment-3
# Python Program: Factorial Calculator & Math Module Operations

This project contains two Python tasks demonstrating the use of functions and Python's built-in math module:

1. ✅ Factorial Calculator – Computes the factorial of a number using a custom function.
2. ✅ Math Module Calculations – Performs square root, natural logarithm, and sine calculations on user input.

---

## 📌 Task 1: Calculate Factorial Using a Function

### 🧾 Problem Statement:
Write a Python program that:
1. Defines a function named factorial that takes a number as an argument.
2. Calculates its factorial using a loop or recursion.
3. Returns the calculated factorial.
4. Calls the function with a sample number and prints the output.

### 🧠 Example Logic:
```python
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example call
print("The factorial of 5 is", factorial(5))......................# 🧮 Math Operations Using Python's math Module

This project is a simple Python script that demonstrates the use of the built-in math module to perform various mathematical operations based on user input.

---

## 📌 Problem Statement

Write a Python program that:

1. Asks the user for a number as input.
2. Uses the math module to calculate:
   - Square root of the number
   - Natural logarithm (log base e)
   - Sine of the number (in radians)
3. Displays the calculated results.

---

## 🧠 How It Works

- The program prompts the user to input a number.
- It then uses the following functions from the math module:
  - math.sqrt(number) for square root
  - math.log(number) for natural logarithm
  - math.sin(number) for sine (in radians)
- Results are printed clearly with labels.
