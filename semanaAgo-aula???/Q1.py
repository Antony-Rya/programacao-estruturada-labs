'''
1-Faça um programa que preencha por leitura um vetor de 5 posições, 
e informe a posição em que um valor x (lido do teclado) está no vetor. 
Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
Leia um número do teclado
Compare se este número está na lista
'''
def criarLista():
    lista = []
    for i in range(5):
        valor = int(input(f"Digite o valor {i}: "))
        lista.append(valor)
    return lista
    
def procurarNumero(lista, numero):
    
    posicao = -1
    for i, v in enumerate(lista):
        if v == numero:
            posicao = i
            break
    print(posicao)
criarLista()

lista = criarLista()

numero = int(input(f"Digite o valor a ser buscado: "))
posicao = procurarNumero(lista, numero)