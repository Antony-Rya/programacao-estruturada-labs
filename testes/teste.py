import random
contador = 1
indexador = 0
lista = ["😒", "👍", "👏", "✌", "🤞", "🤷‍♂️", "🎶"]
while contador <= 5:
    indexador = random.randint(0, len(lista))
    # print(random.choice(lista))
    # contador +=1
    print(lista[indexador])
    contador +=1