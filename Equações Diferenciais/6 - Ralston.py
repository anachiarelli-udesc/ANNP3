def ralston(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + 0.75 * h, y0 + 0.75 * h * m1)
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield[x0, y0]
        
def f(x, y):
    return y * (2 - x) + x + 1
    
x0 = 0.415
y0 = 2.743
h = 0.198
n = 10

r = ralston(f, x0, y0, h, n)

for yi in r:
    print(yi[1])
