'''
4-Dada uma lista de números, utilize map() com uma função lambda para criar 
uma nova lista onde cada número é multiplicado por 2, mas apenas se for maior que 5

Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
Utilize a função map e uma função lambda para multiplicar por 2 os números maiores que 5
'''
def dobrarLista():
    lista = (range(10))

    for i in lista:
        nova_lista = map(lambda x: x * 2, lista)
    print(list(nova_lista))