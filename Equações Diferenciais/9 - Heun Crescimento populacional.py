def heun(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1 + m2) / 2
        x0 += h
        yield[x0, y0]
        
def f(x, y):
    lamb = 0.0487
    v = 25022 
    return lamb * y - v
    
x0 = 0
y0 = 1213335
h = 0.0625
n = int(1 / h)

r = heun(f, x0, y0, h, n)

for yi in r:
    print(yi[1])
