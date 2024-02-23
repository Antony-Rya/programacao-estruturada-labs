palavra = input("Digite uma palavra: ")
teste = palavra[::-1]
if palavra == teste:
    print("É um palindromo")
else:
    print("Não é.")