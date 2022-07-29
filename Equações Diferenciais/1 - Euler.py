def euler(f, x0, y0, h, n):
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        print(f"y{k+1} = {y0}")
        
if __name__ == '__main__':
    def f(x, y):
        return y * (1 - x) + x + 2

x0 = 1.358
y0 = 1.247
h = 0.125
n = 10

euler(f, x0, y0, h, n)
