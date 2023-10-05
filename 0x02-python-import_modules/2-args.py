#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args) - 1
    if num_args == 1:
        print("0 argument(s).")
    else:
        if num_args == 2:
            print("1 argument:")
        else:
            print("{} argument(s): ".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.arg[i]))
