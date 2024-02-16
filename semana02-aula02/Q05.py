#Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área e o perímetro desse círculo. Imprima os resultados formatados.
pi = 3.14
raio = float(input("Digite o raio do circulo: "))

print("A Area é: " , pi * raio ** 2)
print("O perimetro é: " , 2 * pi * raio)