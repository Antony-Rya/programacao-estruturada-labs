# q3

soma = 0
cont = 0
nota = 0
while True:
    nota = float(input())
    if nota == -1:
        break
    if nota in range(0, 11):
        soma += nota
        cont += 1
    else:
        print("Nota invalida")
        
if cont> 0:
    print(soma/cont)