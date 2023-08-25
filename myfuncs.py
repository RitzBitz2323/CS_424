def sqrt(x):
    s= 1.0
    for k in range(100):
        s = (s + x/s)/2
    return s

def expo(x):
    e= 2.7182818284590451
    expx = e**x
    return expx

def ln(x):
    import math
    s = x * 1.0
    for k in range(1000):
        s = s - 1 + x * math.exp(-s)
    return s


