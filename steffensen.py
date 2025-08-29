import numpy as np

#definimos la funcion de la que queremos hallar la raiz

def func(x):
    return 0.5*np.sin(x/2) + np.pi  #colocamos nuestro g(x)


#definimos una funcion para el metodo que solicita "a" (nuestro limite inferior del intervalo), "b" (lim sup) y 'tol' (tolerancia)
def punto_fijo(a, b, tol):
    
    r_1 = 0 #valor de la iteracion anterior, como no hemos hecho ninguna, vale 0
    r = (a + b)/2 #valor de la raiz (que convergera luego al valor verdadero)
    fr = func(r) #la funcion evaluada en la raiz
    eps = r - r_1 #diferencie entre la raiz y a raiz anterior, queremos que sea menos que la tolerancia
    
    if fr == r: #si el primer valor es la raiz, retornamos 'r'
        return print(r)
    
    while eps > tol: #mientras el error sea mayor a la tolerancia, seguir ejecutando
        r_1 = r     #guardamos el valor de la raiz en la iteracion anterior en la variable r_1
        r = fr      #actualizamos el valor de la raiz en el valor de la funcion evaluada en el anterior valor de r
        fr = func(r) #calculamos fr en el nuevo valor de r
        eps = abs(r - r_1) #calculamos el error
    
    return print(r) #retornamos la raiz


punto_fijo(0, 2*np.pi, 10**-5)