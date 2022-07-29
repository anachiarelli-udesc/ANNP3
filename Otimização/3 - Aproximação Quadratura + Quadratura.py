import numpy as np
import math

a = 0.057
b = 2.087
xs = [0.644, 1.339, 1.697]

def f(x):
    return x * math.sin(4 * x * math.cos(math.log(1 + x**2)))

def f1(x):
    return 1
    
def f2(x):
    return x
    
def f3(x):
    return math.cos(x)

def f4(x):
    return x**2
    
def f5(x):
    return math.sin(x)
    
def f6(x):
    return x**3

def f7(x):
    return math.cos(2*x)
    
def f8(x):
    return x**4
    
def f9(x):
    return math.sin(3*x)
    
    
funcs = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

#Raízes do polinômio de Legendre de grau 12
pontos_n12 = [-0.1252334085114689, 0.1252334085114689, -0.3678314989981802, 0.3678314989981802, -0.5873179542866175, 0.5873179542866175, -0.7699026741943047, 0.7699026741943047, -0.9041172563704749, 0.9041172563704749, -0.9815606342467192, 0.9815606342467192]
pesos_n12 = [0.24914704581340277, 0.24914704581340277, 0.2334925365383548, 0.2334925365383548, 0.20316742672306592, 0.20316742672306592, 0.16007832854334622, 0.16007832854334622, 0.10693932599531843, 0.10693932599531843, 0.04717533638651183, 0.04717533638651183]

def quadratura(f, x:list, c:list):
   return sum([ci * f(xi) for ci, xi in zip(c, x)])
    
def change(f,a,b):
   def g(u):
      return f((b+a)/2 + (b-a)*u/2) * (b-a)/2
   return g
    
def best_func(f, funcs, a, b):
    k = len(funcs)
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []
    
    for i in range(0, k):
        for j in range(0, k):
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)
                g = change(f_ij, a, b)
                integral_ij = quadratura(g, pontos_n12, pesos_n12)
                A[i][j] = integral_ij
            else:
                A[i][j] = A[j][i]
        # matriz B:
        def ffi(x):
            return f(x) * funcs[i](x)
        w = change(ffi, a, b)
        B.append(quadratura(w, pontos_n12, pesos_n12))
    return np.linalg.solve(A, B)


coeffs = best_func(f, funcs, a, b)
# imprime os coeficientes:
for i in range(len(coeffs)):
    print(f"c{i+1}: {coeffs[i]}")
    
# calculando g(x)
def g(x):
    return f1(x) * coeffs[0] + f2(x) * coeffs[1] + f3(x) * coeffs[2] + f4(x) * coeffs[3] + f5(x) * coeffs[4] + f6(x) * coeffs[5] + f7(x) * coeffs[6] + f8(x) * coeffs[7] + f9(x) * coeffs[8]
 
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
