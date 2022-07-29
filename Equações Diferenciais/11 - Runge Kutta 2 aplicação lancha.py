import math

def RK2(f, x0, y0, h, n, b):
    for _ in range(n):
        a = 1 -b
        q = p = 1/(2*b)
        m1 = f(x0, y0)
        m2 = f(x0 + p * h, y0 + q * h * m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield[x0, y0]
    
    
def f(x, y):
    a = 8.639
    return - (y/math.sqrt((a**2) - (y**2)))
    
x0 = 1.079
y0 = 4.917
b = 0.907
h = 0.228
n = 10


r = RK2(f, x0, y0, h, n, b)

for yi in r:
    print(yi[1])
