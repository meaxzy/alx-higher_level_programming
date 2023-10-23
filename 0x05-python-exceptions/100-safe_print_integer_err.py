#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    print()
    except (ValueError, TypeError):
        print(error_message, file=sys.stderr)
        return False
