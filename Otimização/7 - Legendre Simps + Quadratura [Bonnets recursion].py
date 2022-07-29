import numpy as np
import math

a = -1
b = 1
n = 128
xs = [-0.691, 0.25, 0.843]
grau_legendre = 12

def f(x):
    return x * math.cos(10 * x**2 * math.exp(-x**2))

def simps(f, a, b, n):
    if (n % 2 != 0):
        raise ValueError("O número de subintervalos deve ser par")
    soma = 0
    numParabolas = int(n/2)
    h = (b-a) / n
    for k in range(numParabolas):
        x0 = a + (2 * k) * h
        x1 = a + (2 * k + 1) * h
        x2 = a + (2 * k + 2) * h
        soma += (f(x0) + 4 * f(x1) + f(x2))
    soma *= h/3.0
    return soma
    
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
for i in range(grau_legendre):
    numer = simps(lambda x: f(x) * P(i, x), a, b, n)
    denom = simps(lambda x: P(i, x) * P(i, x), a, b, n)
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
    
    
    
