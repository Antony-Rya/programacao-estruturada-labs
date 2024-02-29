#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

soma = n1+n2
print("A soma de {} e {} é {} .".format(n1, n2, soma))
sub = n1 - n2
print("A subtração de {} e {} é {} .".format(n1, n2, sub))
mult = n1 * n2
print("A subtração de {} e {} é {} .".format(n1, n2, mult))
div = n1 // n2
print("A subtração de {} e {} é {} .".format(n1, n2, div))

