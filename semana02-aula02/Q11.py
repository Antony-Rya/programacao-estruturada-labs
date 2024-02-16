#Escreva um programa que solicite ao usuário dois números e verifique se o primeiro número é maior que o segundo. Imprima uma mensagem informando o resultado da comparação.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
if n1 > n2: 
    print(n1, " é maior que ", n2)
else:
    print(n2, " é maior que ", n1)
