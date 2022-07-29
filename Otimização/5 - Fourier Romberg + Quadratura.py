from math import cos, sin, exp, pi, ceil

a = -3.141592653589793
b = 3.141592653589793
h = 2 * pi / 16
k = int(8 / 2)
xs = [-1.538, -0.387, 1.461]

def f(x):
    return x * sin(10 * x**2 * exp(-x**2))
    
def romberg(col1):
    col1 = [item for item in col1]
    n = len(col1)
    for j in range (n-1):
        temp_col = [0] * (n - 1 - j)
        for i in range (n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * col1[i + 1] - col1[i]) / (4 ** power - 1)
        col1[:n - 1 - j] = temp_col
    return col1[0]

def trapz(f, a, b, h):
    n = int((b - a) / h)
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h/2

hs = [h / 2** i for i in range(k)]
col1 = [trapz(f, a, b, hi) for hi in hs]
coeffs = []

c = (1/(2 * pi)) * romberg(col1)
coeffs.append(c)

for m in range(1, 11):
    col1a = [trapz(lambda x: f(x) * cos(m * x), a, b, hi) for hi in hs]
    am = (1/pi) * romberg(col1a)
    coeffs.append(am)
    col1b = [trapz(lambda x: f(x) * sin(m * x), a, b, hi) for hi in hs]
    bm = (1/pi) * romberg(col1b)
    coeffs.append(bm)
    
for i in range(len(coeffs)):
    print(f"c{i+1} = {coeffs[i]}")
print("-------------------\n")
    
def g(x, coeffs):
    soma = coeffs[0]
    for i in range(1, len(coeffs), 2):
        soma += coeffs[i] * cos(ceil(i/2)*x)
        soma += coeffs[i+1] * sin(ceil(i/2)*x)
    return soma

for xi in xs:
    print(f"x{xi} = {g(xi, coeffs)}")
    
# calculando o erro com o método da quadratura gaussiana: 
# com 10 nós (mudar se necessário)
pontos_n10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
pesos_n10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
n10 = zip(pontos_n10, pesos_n10)

# MUDAR a função do erro para a função que está dentro da integral
def func_erro(x):
    return pow((f(x) - g(x, coeffs)), 2)

def quadratura_zip(func_erro, pontos_e_pesos):
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k * func_erro(x_k)
    return soma
    
def change_zip(func_erro, a, b, u):
    return func_erro((b+a)/2 + (b-a)*u/2) * (b-a)/2
    
def g_erro(u):
    return change_zip(func_erro, a, b, u)
    
erro = quadratura_zip(g_erro, n10)

#imprimindo o erro:
print("-------------------\n")
print("Erro: ", erro)
    
