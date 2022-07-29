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
    return y * (1 - x) + x + 2
    
x0 = 1.184
y0 = 1.707
b = 0.641
h = 0.121
n = 10

r = RK2(f, x0, y0, h, n, b)

for yi in r:
    print(yi[1])
