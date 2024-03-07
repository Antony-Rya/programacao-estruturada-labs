# A = int(input("Digite o valor de um lado: "))
# B = int(input("Digite o valor de um lado: "))
# C = int(input("Digite o valor de um lado: "))
# if (A < B + C) and (B < A + C) and (C < A + B):
#     if (A == B and B == C):
#         triangulo = "Equilatero"
#     elif (A != B and B != C and A != C):
#         triangulo = "Escaleno"  
#     else:
#         triangulo = "Isosceles"
#     print("Esse triangulo é valido e é um triangulo", triangulo)
# else:
#     print("Esse triangulo é invalido")

# # if (A == B or B == C or A == C):
# #       print("È um triangulo isosceles")

lista = input("Digite os três lados de um triangulo: ").split(" ")
# A, B, C = int(lista.index[0, 1, 2])
A, B, C = [lista[i] for i in (1, 3, 5)]
print(A)
