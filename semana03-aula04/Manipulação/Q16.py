#Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome.
nome = input("Digite seu nome completo: ")
lista = nome.split(" ")
primeiro_nome = lista[0]
print("Seu primeiro nome é: ", primeiro_nome)