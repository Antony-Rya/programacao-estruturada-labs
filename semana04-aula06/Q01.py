#Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.
num = int(input("Digite um numero: "))
if num > 0:
    print("Positivo.")
elif num == 0:
    print("Zero.")

else:
    print("Negativo.")