lista1 = [1, 3, 5]
lista2 = [2, 4, 6, 8, 10]

new_lista = []
cont = 0
maior_lista = lista1 if len(lista1) > len(lista2) else lista2
menor_lista = lista1 if len(lista1) < len(lista2) else lista2
for i in (range(len(maior_lista))):
    if i < len(maior_lista):
        new_lista.append(lista1[i])
        new_lista.append(lista2[i])
    else:
        new_lista.append(maior_lista[i])
print(new_lista)