#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".
palavra = input("Digite uma palavra: ")
palavraMin = palavra.lower()
invertidaMin = palavraMin[::-1]
if palavraMin == invertidaMin:
    print("É um palindromo")
else:
    print("Não é.")