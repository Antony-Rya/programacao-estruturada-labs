#Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas vezes uma determinada letra aparece na frase.
frase = input("Digite uma frase: ")
letra = input("Escolha uma letra")
quantidade = frase.count(letra)
print(f"Essa letra aparece {quantidade} vezes.")