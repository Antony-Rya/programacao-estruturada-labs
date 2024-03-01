#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python".
frase = input("Digite uma frase: ")
if frase.find("Python") or frase.find("python") != -1:
    print("Tem a palavra 'Python' ")
else:
    print("Não tem a palavra 'Python' ")