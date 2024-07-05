# Exercício 10: Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta. Quando a senha estiver correta, imprima uma mensagem de boas-vindas.
senha = "1234"
acertou = False
while not acertou:
    tentativa_senha = input("Digite uma senha: ")
    if tentativa_senha == senha:
        print("Bem-vindo")
        acertou = True
    else:
        print("Senha errada, tente novamente.")
