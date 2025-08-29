import numpy as np
import sympy as smp #para calcular la derivada y evaluar automaticamente


#colocamos nuestra funcion y la devolvemos evaluada en un 'x'
y = smp.symbols('y') #definimos x como variable
g = smp.log(y-1) + smp.sin(y-1) #funcion a utilizar

#derivamos la funcion y la devolvemos evaluada en un 'x'
def pr_func(a, b):     #'a' es la funcion a derivar y 'b' el punto donde evaluamos
    pr_g = smp.diff(a) #derivamos 'a'
    return pr_g.subs(y, b).n()

#definimos la funcion del metodo
def new_raph(c, d, tol): #'c' el valor inf de I, 'd' valor sup de I, 'tol'  nuestra tolerancia
    x_1 = 0 #nuestro valor de la iteracion anterior, como no hemos hecho ninguna, vale 0
    x = c #nuestro punto de inicio, esto puede variar y por defecto usaremos el punto medio de I
    fx = g.subs(y, c).n() #la funcion evaluada en nuestro primer punto
    eps = abs(x - x_1) #nuestro error, queremos que sea menos que la tolerancia
    if fx == 0:
        return x #si el primer evaluado resulta ser una raiz, devolvemos el valor

    #ejeuctamos hasta que nuestro error sea menos a la tolerancia
    while eps > tol:
        x_1 = x #guardamos nuestro anterior valor de x
        fx = g.subs(y, x_1).n() #guardamos el anterior valor de la funcion
        pr_fx = pr_func(g, x_1) #calculamos la derivada con el valor anterior
        x = x_1 - fx/pr_fx #calculamos el nuevo valor de la iteracion
        eps = abs(x - x_1) #calculamos el error

    return print(x)

new_raph(1.3, 2, 10**-12)