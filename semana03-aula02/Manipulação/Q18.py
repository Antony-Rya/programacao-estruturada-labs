#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.

frase = input("Digite uma frase: ")
if frase[-1] == ".":
    print("Tem ponto final.")
else:
    print("Tem ponto final não.")