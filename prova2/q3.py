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
    pares, impares = [], []
    antigo_pares, antigo_impares = 0, 0
    for i in lista:
        if i % 2 == 0:
            if len(pares) > 5:
                pares.pop(antigo_pares)
                pares[antigo_pares] = i
                antigo_pares += 1
            else: 
                pares.append(i)
        else:
            if len(impares) > 5:
                if len(pares) > 5:
                    impares.pop(antigo_pares)
                    pares[antigo_impares] = i
                    antigo_pares += 1
                else: 
                    impares.append(i)
    return pares, impares

lista = ler_valores()
pares, impares = processa_lista(lista)
print(f"{pares}\n{impares}")
