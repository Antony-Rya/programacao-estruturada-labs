# q3
numero = int(input(""))
lista = []
soma = 0
exemplo = ""
for i in range(1, numero + 1):
    exemplo = f"{i}/{i*3}"
    lista.append(exemplo)
    soma += i/i*3
print(lista)
print(f"{soma:,2f}")