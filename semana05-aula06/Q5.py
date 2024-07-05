# Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".
vogais = 0
frase = input("Digite uma frase: ")
for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogais += 1
print(vogais)
        
