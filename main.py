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

    if bool(email.find("@")) and bool(email.find(".com")) and (bool((email.find(" ")) == False)) and (bool(email.find("@.") == False)):
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
    11-Escreva uma função em Python function que aceita uma string e 
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


def len_custom(iteravel):
    '''
    12-Crie uma função chamada len_custom que aceita 
    um iterável (por exemplo, uma lista ou uma string) 
    como argumento e retorna o número de elementos no iterável. 
    Ela deve ter o mesmo comportamento que a função embutida len().
    '''
    cont = 0
    for _ in iteravel:
        cont += 1
    return cont

def sum_custom(numeros):
    '''
    12-Crie uma função chamada sum_custom que aceita 
    uma lista de números como argumento e retorna a soma 
    de todos os números na lista. Ela deve ter o mesmo 
    comportamento que a função embutida sum().
    '''
    soma = 0
    for i in numeros:
        soma += i

    return soma

def max_custom(lista):
    '''
    Crie uma função chamada max_custom que aceita uma 
    lista de números como argumento e retorna o maior 
    número na lista. Ela deve ter o mesmo comportamento 
    que a função embutida max().
    '''
    if len(lista) == 0:
        return None
    A = lista[0]
    B = lista[1]
    C = lista[2]
    maior = 0
    if A > B and A > C:
        maior = A
    elif B > A and B > C:
        maior = B
    else:
        maior = C
    return maior

def min_custom(lista):
    '''
    15-Crie uma função chamada max_custom que aceita uma 
    lista de números como argumento e retorna o maior 
    número na lista. Ela deve ter o mesmo comportamento 
    que a função embutida max().
    '''
    if len(lista) == 0:
        return None
    A = lista[0]
    B = lista[1]
    C = lista[2]
    menor = 0
    if A < B and A < C:
        menor = A
    elif B < A and B < C:
        menor = B
    else:
        menor = C
    return menor

def startswith_custom(string, prefixo):
    '''
    16-Crie uma função chamada startswith_custom que aceita 
    uma string e um prefixo como argumentos e retorna True 
    se a string começar com o prefixo, caso contrário, retorna 
    False. Ela deve ter o mesmo comportamento que o método str.
    startswith().
    '''
    for i, v in enumerate(prefixo):
        if string[i] == v:
            continue
        else:
            return False
    return True

    # if len(prefixo) > 1:
    #     if string[0] == prefixo[0]:
    #         if string[1] == prefixo[1]:
    #             return True
    # else:
    #     return False
    # if string[0] == prefixo[0]:
    #     return True
    # else:
    #     return False
    
def endswith_custom(string, sufixo):
    '''
    17-Crie uma função chamada endswith_custom que 
    aceita uma string e um sufixo como argumentos e retorna 
    True se a string terminar com o sufixo, caso contrário, 
    retorna False. Ela deve ter o mesmo comportamento que o 
    método str.endswith().
    '''
    for i, v in enumerate(sufixo):
        if string[-i] == v:
            continue
        else:
            return False
    return True

    # if len(sufixo) > 1:
    #     if string[-1] == sufixo[-1]:
    #         if string[-2] == sufixo[-2]:
    #             return True
    #         else: 
    #             return False
    #     else: 
    #         return False
    # else:
    #     if string[0] == sufixo[0]:
    #         return True
    #     else:
    #         return False

def split_custom(string, separador):
    '''
    18-Crie uma função chamada split_custom que aceita 
    uma string e um caractere de separação como argumentos 
    e retorna uma lista de substrings separadas pelo caractere 
    de separação. Ela deve ter o mesmo comportamento que o método str.split().
    '''
    lista = []
    pointer = 0
    for i in string:
        atual = string.index(i)
        if i == separador:
            
            lista.append(string[pointer:atual])
            pointer = string.index(i)+1
        elif i == string[-1]:
            lista.append(string[pointer])
    return lista
def strip_custom(string, caracteres):

    '''
    19-Crie uma função chamada strip_custom que aceita 
    uma string e caracteres de remoção como argumentos 
    e retorna uma nova string com os caracteres de remoção 
    removidos dos extremos da string. Ela deve ter o mesmo 
    comportamento que o método str.strip().
    '''
    newstring = ""
    for i in string:
        if i != caracteres:
            newstring += i
    return newstring

def replace_custom(string, substring, substringN):
    '''
    20-Crie uma função chamada replace_custom que 
    aceita uma string, uma substring antiga e uma substring 
    nova como argumentos e retorna uma nova string com todas as 
    ocorrências da substring antiga substituídas pela substring 
    nova. Ela deve ter o mesmo comportamento que o método str.replace().
    '''
    tamanho = len(substring)
    newstring = ""
    idx = string.index(substring)
    plot = string[0:idx]
    plot2 = string[idx+tamanho:]
    newstring = plot + substringN + plot2
    return newstring

# def 
#     '''
#     21-Crie uma função que aceita *args e retorna a 
#     soma de todos os números passados como argumentos.
#     '''