def eulermid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + h/2 * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0
    
if __name__ == '__main__':
    def f(x, y):
        return 0.0594 * y + 49587

x0 = 0
y0 = 1005819
h = 0.0625
n = int(1 / h)

r = eulermid(f, x0, y0, h, n)

for yi in r:
    print("%.15f" % yi[1])
