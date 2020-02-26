def ord (lista):
    orden=[]
    for i in range(0,len(lista)):
        a=min(lista)
        b=lista.index(min(lista))
        lista.pop(b)
        orden.append(a)
    return orden

print(ord([3,9,6]))
