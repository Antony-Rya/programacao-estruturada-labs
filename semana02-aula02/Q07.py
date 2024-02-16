#Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. Calcule e imprima o salário anual.

salario = float(input("Digite seu salario mensal: "))
meses = int(input("Digite quantos meses trabalhados por ano: "))
print("Seu salario anual é", salario * meses, "R$")