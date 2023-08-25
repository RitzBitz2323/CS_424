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


import math

print("--------D E M O   M Y F U N C S . P Y-------")
print("my function ", sqrt(3.7))
print("math function", math.sqrt(3.7))
print("---------------")
print("my function ", expo(3.7))
print("math function", math.exp(3.7))
print("---------------")
print("my function ", ln(3.7))
print("math function", math.log(3.7))
print("---------------")