'''
5-Faça um programa que converta uma lista de temperaturas de Fahrenheit para 
Celsius, em seu programa o usuário deverá inserir uma sequência de valores que 
representam a temperatura em graus Fahrenheit, seu programa deve receber esses 
valores e armazenar em uma lista até que o valor inserido pelo usuário seja um 
valor em branco (uma string vazia). Converta todos os valores presentes na lista 
para graus Celsius usando a função map e imprima na tela em uma formatação amigável 
ao usuário.

Utilize o while e no bloco de repetição leia dados de temperatura do usuário
Acrescente os dados na lista
Crie uma função para converter temperatura de Farenheint para Celcios
Use a função map com a função e a lista
Imprima todas os valores da nova lista
'''
lista = []

while True:
    numero = input('Digite uma temperatura: ')
    if numero != '':
        lista.append(float(numero))
    else:
        break

nova_lista = map(lambda x: (x-32)*3/9, lista)
print(lista)
nova_lista = list(nova_lista)
for i in range(len(nova_lista)):
    nova_lista[i] = float(f'{nova_lista[i]:.2f}')
print(nova_lista)

