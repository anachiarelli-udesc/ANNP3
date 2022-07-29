def euler(f, x0, y0, h, n):
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        print(f"y{k+1} = {y0}")
        
if __name__ == '__main__':
    def f(x, y):
        return 0.0357 * y

x0 = 0
y0 = 1631542
h = 0.0625
n = int(1 / 0.0625)

euler(f, x0, y0, h, n)
