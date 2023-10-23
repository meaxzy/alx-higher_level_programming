#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(integer_value))
        return True
    except (ValueError, TypeError):
        error_message = "Exception: Value is not an integer"
        print(error_message, file=sys.stderr)
        return False
