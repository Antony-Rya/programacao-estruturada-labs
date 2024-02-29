#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
nomecompleto = input("Dogote seu nome completo: ")
partesnome = nomecompleto.split(" ")
primeironome = partesnome[0]
segundonome = partesnome[1]
terceironome = partesnome[2]
inicial1 = primeironome[0:1]
inicial2 = segundonome[0:1]
inicial3 = terceironome[0:1]

iniciais = inicial1 + "." + inicial2 + "." + inicial3
print(iniciais)