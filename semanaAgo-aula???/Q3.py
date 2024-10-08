from Q2 import gerar_lancamentos

'''
Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma: cada célulaé a soma dela mesma e das células anteriores. Imprima o vetor antes e depois da manipulação. Exemplo:

Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]
'''

tamanho = 10
numeros = gerar_lancamentos(0, 20, tamanho)

soma = 0

for i in range(tamanho):
    numeros[i] += soma
    for j in range(i, -1, -1):
        soma += numeros[j]
    numeros[i] += soma
    soma = 0
print(numeros)