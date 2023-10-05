#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    c = cal.add(a, b)
    d = cal.sub(a, b)
    e = cal.mul(a, b)
    f = cal.div(a, b)
    print("{} + {} = {}".format(a, b, c))
    print("{} - {} = {}".format(a, b, d))
    print("{} * {} = {}".format(a, b, e))
    print("{} / {} = {}".format(a, b, f))
