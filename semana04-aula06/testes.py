A = int(input("Digite o valor de um lado: "))
B = int(input("Digite o valor de um lado: "))
C = int(input("Digite o valor de um lado: "))
if (A < B + C) and (B < A + C) and (C < A + B):
    if (A == B and B == C):
        triangulo = "Equilatero"
    if (A != B and B != C):
        triangulo = "Escaleno"  
    else:
        triangulo = "Isosceles"
    print("Esse triangulo é valido e é um triangulo", triangulo)
else:
    print("Esse triangulo é invalido")