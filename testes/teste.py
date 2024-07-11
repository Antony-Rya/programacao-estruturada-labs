# q3

soma = 0
cont = 0
nota = 0
while True:
    nota = float(input())
    if nota == -1:
        break
    if nota not in range(0, 11):
        print("Nota invalida")
        continue
   
    soma += nota
    cont += 1
       
        
if cont> 0:
    print(soma/cont)