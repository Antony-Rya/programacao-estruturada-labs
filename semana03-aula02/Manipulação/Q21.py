#Escreva um programa que solicite ao usuário para digitar seu nome e imprima-o em formato invertido. Por exemplo, se o nome for "João Silva", o programa deve imprimir "avliS oãoJ".
frase = input("Digite uma frase: ")
frase_nova = frase[::-1]
print(frase_nova)
