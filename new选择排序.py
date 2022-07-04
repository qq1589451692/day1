lista=[23,23,50,12,10,12,30]
for i in range(len(lista)-1):
    index=lista.index(min(lista[i:]),i)
    lista[i],lista[index]=lista[index],lista[i]
    print(lista)