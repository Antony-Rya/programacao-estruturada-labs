'''
2-Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.

Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
Faça uma iteração na lista para verificar quantos destes números são iguais à 6
'''

def gerar_lancamentos(min, max, tamanho):
    numeros = []
    for _ in range(tamanho):
        from random import randint
        numeros.append(randint(min, max))
    return numeros

def porcentagemFaces(lista, numero):
    total = len(lista)
    quantidade = 0
    for n in lista:
        if n == numero:
            quantidade += 1
    return quantidade, f"{quantidade/total}"

if __name__ == "__main__":  
    numeros = gerar_lancamentos(1, 6, 50)
    quantidade, porcentagem_6 = porcentagemFaces(numeros, 6)
    print(quantidade)
    print(porcentagem_6)       

