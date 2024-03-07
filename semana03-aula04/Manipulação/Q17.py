#Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas palavras existem na frase.
frase = input("Digite uma frase: ")
quant = frase.count(" ") + 1
print("São ", quant, "palavras")