#Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").
email = input("Digite seu e-mail: ")
usuario = email[:email.index("@")]
dominio = email[email.index("@")+1:email.index(".")]
print(f" Seu usuario é {usuario} e seu dominio é {dominio}")