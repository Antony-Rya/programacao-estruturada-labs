'''
7 - Escreva um programa em Python para calcular a soma de todos os elementos de cada 
tupla armazenada dentro de uma lista de tuplas.

Lista original de tuplas:

[(1, 2), (2, 3), (3, 4)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[3, 5, 7]

Lista original de tuplas:

[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[9, -1, 7, 8]
'''

tuplas = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

nova_lista = []

for i in tuplas:
    soma = 0
    for k in i:
        soma += k
    nova_lista.append(soma)

print(nova_lista)