def RK4(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        m3 = f(x0 + (h/2), y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        yield[x0, y0]
    
    
def f(x, y):
    return y * (1 - x) + x + 2
    
x0 = 1.726
y0 = 1.618
h = 0.118
n = 10

r = RK4(f, x0, y0, h, n)

for yi in r:
    print(yi[1])
