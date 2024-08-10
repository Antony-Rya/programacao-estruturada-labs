def saudacao(nome):
    '''
    1-Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".
    '''
    return f"Olá, {nome}!"

def dobro(num):
    '''
    2-Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
    '''
    return num*2

def saudacao_personalizada(nome, idioma):
    '''
    3-Crie uma função chamada saudacao_personalizada que aceita 
    um nome e um idioma como argumentos. O idioma é opcional 
    e padrão para "inglês". A função deve retornar uma saudação 
    no idioma especificado.
    '''
    if idioma == "espanhol":
        return f"Hola, {nome}!"
    elif idioma == "francês":
        return f"Bonjour, {nome}!"
    else:
        return f"Hello, {nome}!"

def potencia(base, expoente):
    '''
    4-Escreva uma função potencia que aceita uma base
    e um expoente (com expoente padrão igual a 2) e
    retorna a base elevada ao expoente
    '''
    if expoente != 2:
        return base**expoente
    else: 
        return base**2


def idade_valida(idade):
    '''
    6-Crie uma função chamada idade_valida que verifica 
    se a idade fornecida como argumento é um número inteiro 
    válido entre 0 e 150.
    '''
    if idade >= 0 and idade <= 150:
        return True
    else:
        return False
    
def validar_email(email):
    '''
    8-Implemente uma função validar_email que verifica se uma 
    string fornecida como argumento representa um endereço de 
    e-mail válido. Considere que um email válido não deve ter 
    espaços, deve conter 01 arroba e terminar com .com
    '''
    # if "@" not in email and ".com" not in email and " " not in email:
    #     if email.indexOf("@" + 1) == ".":
    #         return False
    # else:
    #     return True

    if email.find("@") and email.find(".com") and (email.find(" ") == False):
        if email.find("@.") != -1:
          return True
    else:
        return False

def calcular_pagamento(horas_trabalhadas, taxa_hora):
    '''
    Escreva uma função calcular_pagamento que 
    aceita os parâmetros nomeados horas_trabalhadas 
    e taxa_hora e retorna o pagamento total.
    '''
    return horas_trabalhadas * taxa_hora

def maior_numero(a, b, c):
    '''
    Crie uma função que retorne o maior número dentre 3 elementos.
    '''
    return max(a, b , c)

def contagem_letras(string):
    '''
    Escreva uma função em Python function que aceita uma string e 
    retorna a quantidade de letras maiúsculas e minúsculas.
    '''
    maisculas = 0
    minusculas = 0
    resultado = ()
    for letra in string:
        if letra.isupper():
            maisculas += 1
        else:
            minusculas += 1
    resultado = (maisculas, minusculas)
    return resultado