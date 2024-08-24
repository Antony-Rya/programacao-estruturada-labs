from Q2 import gerar_lancamentos
from random import randint

'''
9 - Você recebe um número inteiro grande representado como um array de inteiros 
chamado 'digits', onde cada 'digits[i]' é o i-ésimo dígito do número. Os dígitos 
são ordenados do dígito mais significativo para o menos significativo na ordem da 
esquerda para a direita. O número inteiro grande não contém zeros à esquerda.

Incremente o número inteiro grande em um e retorne o array resultante de dígitos.

Exemplo 1:

Entrada: digits = [1,2,3] Saída: [1,2,4] Explicação: O array representa o número 123. 
Incrementar um resulta em 123 + 1 = 124. Portanto, o resultado deve ser [1,2,4].

Exemplo 2:

Entrada: digits = [4,3,2,1] Saída: [4,3,2,2] Explicação: O array representa o número 
4321. Incrementar um resulta em 4321 + 1 = 4322. Portanto, o resultado deve ser [4,3,2,2].

Exemplo 3:

Entrada: digits = [9] Saída: [1,0] Explicação: O array representa o número 9. Incrementar 
um resulta em 9 + 1 = 10. Portanto, o resultado deve ser [1,0].
'''

digits = gerar_lancamentos(randint(1, 9), 9, randint(3, 7))
numero = ""
for v in digits:
    numero += str(v)
print(digits)
numero = str(int(numero)+1)
for i in range(len(numero)):
    digits[i] = int(numero[i])
print(digits)
