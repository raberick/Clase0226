# -*- coding: utf-8 -*-
import numpy as np
def ordenar (lista):
    
    n=len(lista)
    a=np.zeros(n)
    for i in range(n):
        
        a[i]=min(lista)
        b=lista.index(min(lista))
        lista[b]=999
    return (a)
        
if __name__ == "__main__":
        
    print (ordenar([5,4,3,2,1,6,7,8,9,10]))