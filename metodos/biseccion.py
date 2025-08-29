import numpy as np
import matplotlib.pyplot as plt
#definimos la funcion de la que queremos hallar la raiz

def func(x):
    return np.exp(x) - x**2 + 3*x - 2  

#definimos una funcion para el metodo que solicita "a" (nuestro limite inferior del intervalo), "b" (lim sup) y 'tol' (tolerancia)

def bis_sect(a, b, tol):
    
    #definimos nuestras variables
    c_1 = 0  #punto medio de la iteracion anterior, como no hemos hecho ninguna, vale 0
    c = (a + b) / 2   #punto medio
    fc = func(c)   #la funcion evaluada en el punto medio (c)
    fa = func(a)   #funcion evaluada en 'a'
    fb = func(b)    #funcion evaluada en 'b'
    eps = abs(fc)   #cuanto error hay en nuestra solucion (queremos que sea menos que nuestra tolerancia) y si vale cero es que
                    #hemos encontrado la raiz directamente
    
    #iteramos hasta que nuestro error sea menor que la tolerancia
    while eps > tol:
        #actualizamos los valores del punto medio, error y la f(c) en cada iteracion
        c = (a + b) / 2
        eps = abs(c - c_1)
        fc = func(c)
        
        #si fa*fc<0, cambiamos el valor de 'b' a 'c'
        if fa*fc < 0:
            b = c
            fb = func(b)
        #si fb*fc<0, cambiamos el valor de 'a' a 'c'    
        elif fb*fc < 0:
            a = c
            fa = func(a)
        #si f(c) es igual a cero hemos encontrado la raiz    
        elif fc == 0:
            return c
        #guardamos el valor de la iteracion para utilizarlo en la siguiente y calcular el error
        c_1 = c
    
    x = np.linspace(c-15, c+15, 50)
    y = func(x)
    plt.plot(x, y, label = 'f(x)')
    plt.plot(c, func(c), 'ro', label = 'raiz', markersize = 3)
    plt.text(c, func(c), f'{c:.15f}', fontsize=10, ha='left', va='top')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafica')
    plt.legend()
    plt.grid(True)
    plt.show()    
    #devolvemos el valor del punto medio
    return print(c)
    
bis_sect(0, 1, 10**-5)    