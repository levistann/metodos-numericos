import numpy as np

def func(x):
    f = np.sqrt(29**2+(47-x)**2) + np.sqrt(41**2+x**2) - 85
    return f

def muller(x_0, x_1, x_2, tol):
    f0 = func(x_0)
    f1 = func(x_1)
    f2 = func(x_2)
    c = f2
    a = ((f0 - f2)*(x_1 - x_2) - (f1 - f2)*(x_0 - x_2))/((x_0 - x_2)*(x_1 - x_2)*(x_0 - x_1))
    b = ((f1 - f2)*(x_0 - x_2)**2 - (f0 - f2)*(x_1 - x_2)**2)/((x_0 - x_2)*(x_1 - x_2)*(x_0 - x_1))
    eps = 1
    if b >= 0:
        k = 2*c/(b + np.sqrt(b**2 - 4*a*c))
        
    else:
        k = 2*c/(b - np.sqrt(b**2 - 4*a*c))
    
    x = x_2 - k
    x_arr = [x_0 , x_1, x_2, x]
    
    for i in range(len(x_arr)):
        if func(x_arr[i]) < tol:
            return x_arr[i]
    
    while eps > tol:
        
        x_0 = x_1
        x_1 = x_2
        x_2 = x
        
        f0 = func(x_0)
        f1 = func(x_1)
        f2 = func(x_2)
        c = f2
        a = ((f0 - f2)*(x_1 - x_2) - (f1 - f2)*(x_0 - x_2))/((x_0 - x_2)*(x_1 - x_2)*(x_0 - x_1))
        b = ((f1 - f2)*(x_0 - x_2)**2 - (f0 - f2)*(x_1 - x_2)**2)/((x_0 - x_2)*(x_1 - x_2)*(x_0 - x_1))
        if b >= 0:
            k = 2*c/(b + np.sqrt(b**2 - 4*a*c))
            
        else:
            k = 2*c/(b - np.sqrt(b**2 - 4*a*c))
            
        x = x_2 - k
        
        eps = abs(x - x_2)
    
    return print(x)
            
muller(2, 4, 5, 10**-12)