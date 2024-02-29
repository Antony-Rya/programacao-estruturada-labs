#Escreva um programa que solicite ao usuário uma palavra e imprima uma mensagem formatada mostrando a palavra em caixa alta e caixa baixa.
palavra = input("Digite uma palavra:")
grande = palavra.upper()
pequena = palavra.lower()
mensagem = "{}\n{}".format(grande, pequena)
print(mensagem)