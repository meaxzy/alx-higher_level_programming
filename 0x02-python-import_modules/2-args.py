#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args)

    if num_args == 1:
        print("0 argument(s).")
    else:
        if num_args == 2:
            print("1 argument:")
        else:
            print("{} argument(s): ".format(num_args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, sys.arg[i]))
