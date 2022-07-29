import numpy as np
import math

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
    
def best_func(f, funcs, a, b, h, ki):
    k = len(funcs)
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []
    
    for i in range(0, k):
        for j in range(0, k):
            # matriz A
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)
                hs = [h / 2** i for i in range(ki)]
                col1 = [trapz(f_ij, a, b, hi) for hi in hs]
                integral_ij = romberg(col1)
                A[i][j] = integral_ij
            else:
                A[i][j] = A[j][i]
        # matriz B:
        def ffi(x):
            return f(x) * funcs[i](x)
        hs = [h / 2** i for i in range(ki)]
        col1 = [trapz(ffi, a, b, hi) for hi in hs]
        B.append(romberg(col1))
        
    return np.linalg.solve(A, B)
    
# MUDAR a f(x) aqui
def f(x):
    return x**2 * math.cos(x * math.sin(math.log(1 + x**2)))

# MUDAR funcs aqui (definir cada uma)
# TODO: utilizar a função de interpretação de string para funções (otimização)
def f1(x):
    return 2
    
def f2(x):
    return x - 1
    
def f3(x):
    return x**2 + 1

def f4(x):
    return x**3 + x - 3
    
def f5(x):
    return 0.5 * x**4 - 3 * x**2 + 1
    
def f6(x):
    return x**5 - 4 * x + 2

def f7(x):
    return x**7-x
    
    
funcs = [f1, f2, f3, f4, f5, f6, f7]

# MUDAR os valores do intervalo [a, b] e a quantidade de subintervalos da regra dos trapézios
a = -2.093
b = 2.074
h = (b-a)/10
k = 4
coeffs = best_func(f, funcs, a, b, h, k)

# imprime os coeficientes:
for i in range(len(coeffs)):
    print(f"c{i+1}: {coeffs[i]}")
    
# calculando g(x)
def g(x):
    return f1(x) * coeffs[0] + f2(x) * coeffs[1] + f3(x) * coeffs[2] + f4(x) * coeffs[3] + f5(x) * coeffs[4] + f6(x) * coeffs[5] + f7(x) * coeffs[6]
  
# MUDAR valores de xs  
xs = [-1.068, -0.079, 1.634]
# imprimindo os valores de g(xi)
print("-------------------")

for i in range(len(xs)):
    print(f"g(x{i+1}) : {g(xs[i])}")
    
# calculando o erro com o método da quadratura gaussiana: 
# com 10 nós (mudar se necessário)
pontos_n10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
pesos_n10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
n10 = zip(pontos_n10, pesos_n10)

# MUDAR a função do erro para a função que está dentro da integral
def func_erro(x):
    return math.pow((f(x) - g(x)), 2)

def quadratura(func_erro, pontos_e_pesos):
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k * func_erro(x_k)
    return soma
    
def change(func_erro, a, b, u):
    return func_erro((b+a)/2 + (b-a)*u/2) * (b-a)/2
    
def g_erro(u):
    return change(func_erro, a, b, u)
    
erro = quadratura(g_erro, n10)

#imprimindo o erro:
print("-------------------\n")
print("Erro: ", erro)
