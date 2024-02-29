#Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada.
import re
frase = input("Digite uma frase: ")
novafrase = re.sub("[aeiou]", "*", frase)
print(novafrase)

