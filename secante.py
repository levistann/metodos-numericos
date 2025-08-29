import numpy as np

def func(x):  #colocamos nuestra funcion
    f = (x-2)**2-np.log(x)
    return f

def sec(a, b, tol):
    x_0 = a #nuestro primer x
    x_1 = b #nuestro segundo x
    fx0 = func(x_0)
    fx1 = func(x_1)    #evaluamos en x_1
    x = x_1 - (fx1*(x_1-x_0))/(fx1-fx0) #calculamos nuestra primera iteracion
    eps = 1 #nuestro error, ponemos valor provicional de 1
    if func(x) == 0: #si nuestra primera iteracion resulta ser la raiz, devolvemos ese valor
        return x
    
    while eps > tol:
        x_0 = x_1
        x_1 = x
        fx0 = func(x_0)
        fx1 = func(x_1)
        x = x_1 - (fx1*(x_1-x_0))/(fx1-fx0)
        eps = x - x_1
    
    return print(x)

sec(np.exp(1), 4, 10**-12)