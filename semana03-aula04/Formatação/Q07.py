#Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem formatada no seguinte formato: "Olá, {nome}! Você tem {idade} anos."
nome = input("Digite seu nome!: ")
idade = input("Digite sua idade!: ")
mensagem = "Olá {}! Você tem {} anos.".format(nome, idade)
print(mensagem)