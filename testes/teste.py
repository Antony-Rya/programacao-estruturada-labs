# q3

soma = 0
cont = 0
nota = 0
while nota != -1:
    nota = float(input())
    if nota in range(0, 11):
        soma += nota
        cont += 1
    else:
        print("Nota invalida")
        break
if cont> 0:
    print(soma/cont)