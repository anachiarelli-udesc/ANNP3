import numpy as np
import math

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h/2
    
def best_func(f, funcs, a, b, n):
    k = len(funcs)
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []
    
    for i in range(0, k):
        for j in range(0, k):
            # matriz A
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)
                integral_ij = trapz(f_ij, a, b, n)
                A[i][j] = integral_ij
            else:
                A[i][j] = A[j][i]
        # matriz B:
        def ffi(x):
            return f(x) * funcs[i](x)
        B.append(trapz(ffi, a, b, n))
    return np.linalg.solve(A, B)
    
# MUDAR a f(x) aqui
def f(x):
    return 2 * math.sin(x) + math.cos(-x**2)

# MUDAR funcs aqui (definir cada uma)
# TODO: utilizar a função de interpretação de string para funções (otimização)
def f1(x):
    return 1
    
def f2(x):
    return x
    
def f3(x):
    return math.pow(x, 2)

def f4(x):
    return math.pow(x, 3)
    
def f5(x):
    return math.pow(x, 4)
    
def f6(x):
    return math.pow(x, 5)
    
funcs = [f1, f2, f3, f4, f5, f6]

# MUDAR os valores do intervalo [a, b] e a quantidade de subintervalos da regra dos trapézios
a = -1.015
b = 2.408
n = 256

coeffs = best_func(f, funcs, a, b, n)

# imprime os coeficientes:
for i in range(len(coeffs)):
    print(f"c{i+1}: {coeffs[i]}")
  
# calculando g(x)
def g(x):
    return f1(x) * coeffs[0] + f2(x) * coeffs[1] + f3(x) * coeffs[2] + f4(x) * coeffs[3] + f5(x) * coeffs[4] + f6(x) * coeffs[5]
  
# MUDAR valores de xs  
xs = [-0.344, 0.345, 2.216]
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
    
