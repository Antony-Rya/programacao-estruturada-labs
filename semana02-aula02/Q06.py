#Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit. Imprima o resultado formatado.

temp = float(input("Digite uma temperatura: "))
print(temp, "° em fahrenheit é: ", temp * 1.8 + 32, "°F")