#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        print("Division by zero is not allowed.")
    finally:
        result = None
        print("Inside result: {}".format(result))
    return result
