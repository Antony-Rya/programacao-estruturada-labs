'''
4-Dada uma lista de números, utilize map() com uma função lambda para criar 
uma nova lista onde cada número é multiplicado por 2, mas apenas se for maior que 5

Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
Utilize a função map e uma função lambda para multiplicar por 2 os números maiores que 5
'''

lista = [i**2 for i in range(1, 11)]
print(lista)
lista2 = map(lambda x: x*2 if x > 5 else x, lista)
print(list(lista2))