def heun(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1 + m2) / 2
        x0 += h
        yield[x0, y0]
        
def f(x, y):
    return y * (2 - x) + x + 1
    
x0 = 1.823
y0 = 0.855
h = 0.129
n = 10

r = heun(f, x0, y0, h, n)

for yi in r:
    print(yi[1])
