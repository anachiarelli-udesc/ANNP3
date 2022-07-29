def ralston(f, x0, y0, h_values, n):
    #h_values = [0.263, 0.251, 0.084, 0.425, 0.198, 0.252, 0.223, 0.209, 0.384, 0.074]
    
    for k in range(n):
        h = h_values[k]
        m1 = f(x0, y0)
        m2 = f(x0 + 0.75 * h, y0 + 0.75 * h * m1)
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield[x0, y0]
        
def f(x, y):
    return y * (2 - x) + x + 1
    
x0 = 0.39
y0 = 1.642
x_values = [0.39, 0.557, 0.778, 1.125, 1.421, 1.63, 1.8, 2.009, 2.323, 2.551, 2.968]
n = 10
h_values = []

for i in range(len(x_values)-1):
    h_values.append(x_values[i+1] - x_values[i])

r = ralston(f, x0, y0, h_values, n)

for yi in r:
    print(yi[1])
