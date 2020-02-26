# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:05:25 2020

@author: Andrés
"""
import numpy as np
import sortRodrigo


##### GENERACIÓN DE LISTAS

# RANDOM
ran=np.random.random(10)
ran=(ran*1000)//1
ran=list(ran)
print("lista aleatoria", ran)
ranrod=sortRodrigo.ordenar(ran)
print(" ROD lista aleatoria ordenada",ranrod)


# INVERTIDA
inv=np.random.random(10)
inv=(inv*1000)//1
inv=list(inv)
inv.sort()
inv.reverse()
print("lista invertida",inv)
ranrod=sortRodrigo.ordenar(inv)
print(" ROD lista invertida ordenada",ranrod)

#QUASIINVERTIDA
qua=inv=np.random.random(10)
qua=(qua*1000)//1
qua=list(qua)
qua.sort()
qua[0]+=1000
print("lista quasiordenada",qua)
ranrod=sortRodrigo.ordenar(qua)
print(" QUA lista aleatoria ordenada",ranrod)

#ALTERNADA
alt=inv=np.random.random(10)
alt=(alt*1000)//1
alt=list(alt)
alt.sort()
temp=list(alt)
n=len(alt)
for i in range (int(n/2)):
    alt[2*i]=temp[i]
    alt[2*i+1]=temp[n-1-i]
print("lista alternada",alt)
altrod=sortRodrigo.ordenar(alt)
print(" ROD lista alternada ordenada",ranrod)


#if __name__=="__main__":
  #  cosas
    