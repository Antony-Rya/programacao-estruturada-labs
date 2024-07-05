# Exercício 9: Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. Em seguida, calcule e imprima a média dos números digitados.
num = 0
cont = 0
while num >= 0:
    num += num
    cont += 1
print(num/cont)