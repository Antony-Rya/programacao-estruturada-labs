def saudacao(nome):
    '''
    1-Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".
    '''
    return f"Olá, {nome}!"

def dobrar(num):
    '''
    2-Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
    '''
    return num*2

def saudacao_personalizada(nome, idioma):
    '''
    Crie uma função chamada saudacao_personalizada que aceita 
    um nome e um idioma como argumentos. O idioma é opcional 
    e padrão para "inglês". A função deve retornar uma saudação 
    no idioma especificado.
    '''
    if nome == "ingles":
        return f"Olá, senhora {nome}!"

