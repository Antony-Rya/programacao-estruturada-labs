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
