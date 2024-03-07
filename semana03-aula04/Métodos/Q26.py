# Escreva um programa que peça ao usuário para digitar uma frase e imprima o número de caracteres na frase.
frase = input("Digite uma palavra: ")
frase_nova = frase.count(" ")
print(len(frase) - frase_nova)