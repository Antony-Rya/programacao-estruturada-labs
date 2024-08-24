from Q2 import gerar_lancamentos

'''
10 - Dado o nó inicial de uma lista ligada ordenada, exclua todos 
os duplicados de forma que cada elemento apareça apenas uma vez. Retorne 
a lista ligada também ordenada.

Exemplo:

Input: head = [1,1,2]

Output: [1,2]

'''
lista = sorted(gerar_lancamentos(1, 10, 10))
print(lista)
for i, k in enumerate(lista):
    if lista.count(k) > 1:
        lista.pop(i)
nova_lista = sorted(lista)
print(nova_lista)