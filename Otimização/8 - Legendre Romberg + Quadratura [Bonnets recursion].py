import numpy as np
import math

a = -1
b = 1
xs = [-0.732, -0.211, 0.885]
ordem_erro = 8
k = int(ordem_erro / 2)
h = 2/16
grau_legendre = 16

def f(x):
    return math.tanh(3 * x) * math.cos(3 * x)

    
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
    
def P(n, x): 
    if(n == 0):
        return 1 # P0 = 1
    elif(n == 1):
        return x # P1 = x
    else:
        return (((2 * n)-1)*x * P(n-1, x)-(n-1)*P(n-2, x))/float(n)

coeffs = []        
# já que são duas a duas ortogonais   
# numer = integral de f(x) * fi(x)
# denom = integral de fi(x) * fi(x)

hs = [h / 2** i for i in range(k)]
for i in range(grau_legendre):
    col1 = [trapz(lambda x: f(x) * P(i, x), a, b, hi) for hi in hs]
    numer = romberg(col1)
    col2 = [trapz(lambda x: P(i, x) * P(i, x), a, b, hi) for hi in hs]
    denom = romberg(col2)
    coeffs.append(numer/denom)
    
# imprime os coeficientes:
for i in range(len(coeffs)):
    print(f"c{i+1}: {coeffs[i]}")

def g(x):
    soma = 0    
    for i in range(grau_legendre):
        mult = coeffs[i] * P(i, x)
        soma += mult
    return soma
print("-------------------\n")
for xi in xs:
    print(f"x({xi}) = {g(xi)}")
    
# calculando o erro com o método da quadratura gaussiana: 
# com 10 nós (mudar se necessário)
pontos_n10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
pesos_n10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
n10 = zip(pontos_n10, pesos_n10)

# MUDAR a função do erro para a função que está dentro da integral
def func_erro(x):
    return pow((f(x) - g(x)), 2)

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
    
    
    
