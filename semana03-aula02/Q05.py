#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".
palavra = input("Digite uma palavra: ")
teste = palavra[::-1]
if palavra == teste:
    print("É um palindromo")
else:
    print("Não é.")