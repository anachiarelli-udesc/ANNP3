def eulermid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + h/2 * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0
    
if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1

x0 = 1.53728
y0 = 2.98696
h = 0.17018
n = 10

r = eulermid(f, x0, y0, h, n)

for yi in r:
    print(yi[1])
