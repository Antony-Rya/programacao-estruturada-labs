'''
6 - A partir do dicionário de nomes e idades de pessoas a seguir, 
faça um programa que imprima em ordem a partir dos nomes das pessoas, 
mostre a soma das idades, a média das idades e a pessoa mais velha.
'''

people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 2000000,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 21,
    "Jill": 32,
    "Jack": 32,
}

def ordenacao_e_soma(dicionario):
    soma = 0
    mais_velha = ""
    media = 0
    maior = 0
    for i in dicionario:
        soma += dicionario[i]
        if dicionario[i] > maior:
            mais_velha = i
            maior = dicionario[i]
            
    return print(sorted(dicionario)), print(soma/len(dicionario)), print(mais_velha) 


ordenacao_e_soma(people)
