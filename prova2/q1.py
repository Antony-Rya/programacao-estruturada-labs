pessoas = {
    "Leonardo": 30,
    "Mariana": 15,
    "Gustavo": 29,
    "Bianca": 32,
    "Vinícius": 18,
    "Amanda": 26,
    "Henrique": 11,
    "Camila": 27,
    "Felipe": 33,
    "Juliana": 30,
}

new_lista = []
for k, v in sorted(pessoas.items()):
    if v > 18:
        new_lista.append(k)


print(new_lista)