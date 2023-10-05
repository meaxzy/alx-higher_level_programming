#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 argument(s).")
        print(".")
    else:
        print("{} argument(s): ".format(num_args)
            for i, arg in enumerate(sys.argv[1:], start=1):
                print("{}: {}".format(i, args))
