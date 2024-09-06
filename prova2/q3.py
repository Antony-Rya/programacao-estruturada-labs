def ler_valores():
    lista = []
    while True:
        num = input()
        if num != '0':
            lista.append(int(num))
        else:
            break
    return lista

def processa_lista(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
            if len(pares) > 5:
                pares.pop(0)
        else:
            impares.append(i)
            if len(impares) > 5:
                impares.pop(0)
    return pares, impares

lista = ler_valores()
pares, impares = processa_lista(lista)
print(f"{pares}\n{impares}")
