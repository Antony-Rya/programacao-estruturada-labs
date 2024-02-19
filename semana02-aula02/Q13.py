#Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.

#Instruções:

#Solicite ao usuário o primeiro número inteiro e armazene-o em uma variável chamada numero1. Solicite ao usuário o segundo número inteiro e armazene-o em uma variável chamada numero2. Troque os valores das variáveis numero1 e numero2 utilizando atribuição múltipla. Imprima os valores atualizados das variáveis utilizando a função print().

numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

print("Valores antes da troca: numero1 = ", numero1, " numero2 = ", numero2)
reserva = numero1
numero1 = numero2 
numero2 = reserva
print("Valores depois da troca: numero1 = ", numero1,"  numero2 = ", numero2)