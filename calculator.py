#!/usr/bin/env python3
"""Terminal-based scientific calculator.

This calculator uses only the built-in `math` module and provides
basic arithmetic plus common scientific functions. It runs in the
terminal and shows a repeating menu until the user exits.
"""

import math
import sys


def get_number(prompt):
    """Prompt the user for a number and validate input.

    Returns a float. Keeps prompting until the user provides a valid
    numeric value or enters an exit keyword which raises SystemExit.
    """
    while True:
        try:
            text = input(prompt).strip()
            if text.lower() in ("q", "quit", "exit"):
                raise SystemExit
            return float(text)
        except ValueError:
            print("Invalid number. Please enter a numeric value or 'q' to quit.")


def get_int(prompt):
    """Prompt the user for an integer (used for factorial)."""
    while True:
        try:
            text = input(prompt).strip()
            if text.lower() in ("q", "quit", "exit"):
                raise SystemExit
            value = int(float(text))
            return value
        except ValueError:
            print("Invalid integer. Please enter an integer value.")


# Basic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


# Scientific operations
def power(a, b):
    return math.pow(a, b)


def sqrt(a):
    if a < 0:
        raise ValueError("Square root of negative number")
    return math.sqrt(a)


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


def log10(a):
    if a <= 0:
        raise ValueError("Logarithm domain error; input must be > 0")
    return math.log10(a)


def ln(a):
    if a <= 0:
        raise ValueError("Natural logarithm domain error; input must be > 0")
    return math.log(a)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial of negative number")
    return math.factorial(n)


def expo(a):
    return math.exp(a)


def print_menu():
    """Display the menu of operations."""
    print("\n--- Python Scientific Calculator ---")
    print("Choose an operation (enter the number):")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Power (a^b)")
    print("6) Square root")
    print("7) sin (radians)")
    print("8) cos (radians)")
    print("9) tan (radians)")
    print("10) log (base 10)")
    print("11) ln (natural log)")
    print("12) factorial")
    print("13) e^x (exponential)")
    print("14) Quit")


def main():
    """Main REPL loop for the terminal calculator."""
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print("Result:", add(a, b))

            elif choice == "2":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print("Result:", subtract(a, b))

            elif choice == "3":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print("Result:", multiply(a, b))

            elif choice == "4":
                a = get_number("Enter numerator: ")
                b = get_number("Enter denominator: ")
                print("Result:", divide(a, b))

            elif choice == "5":
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                print("Result:", power(a, b))

            elif choice == "6":
                a = get_number("Enter number: ")
                print("Result:", sqrt(a))

            elif choice == "7":
                a = get_number("Enter angle in radians: ")
                print("Result:", sin(a))

            elif choice == "8":
                a = get_number("Enter angle in radians: ")
                print("Result:", cos(a))

            elif choice == "9":
                a = get_number("Enter angle in radians: ")
                print("Result:", tan(a))

            elif choice == "10":
                a = get_number("Enter number (>0): ")
                print("Result:", log10(a))

            elif choice == "11":
                a = get_number("Enter number (>0): ")
                print("Result:", ln(a))

            elif choice == "12":
                n = get_int("Enter integer for factorial: ")
                print("Result:", factorial(n))

            elif choice == "13":
                a = get_number("Enter exponent value: ")
                print("Result:", expo(a))

            elif choice == "14" or choice.lower() in ("q", "quit", "exit"):
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from the menu.")

        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Error:", ve)
        except SystemExit:
            print("Exiting...")
            break
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")