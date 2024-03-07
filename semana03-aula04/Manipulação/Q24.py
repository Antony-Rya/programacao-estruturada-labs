#Escreva um programa que solicite ao usuário para digitar uma palavra e verifique se ela é um palíndromo.
palavra = input("Digite uma palavra: ")
palavraMin = palavra.lower()
invertidaMin = palavraMin[::-1]
if palavraMin == invertidaMin:
    print("É um palindromo")
else:
    print("Não é um palindromo.")