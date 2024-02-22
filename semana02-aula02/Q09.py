#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.
E1 = int(input("Digite um valor booleano: "))
E1_bool = bool(E1) 
E2 = int(input("Digite outro valor booleano: "))
E2_bool = bool(E2) 

print("Os dois valores passando pelo operador AND retorna: ", E1_bool and E2_bool)
print("Os dois valores passando pelo operador OR retorna: ", E1_bool or E2_bool)
print("O valor 1 passando pelo operador NOT retorna: ", not E1_bool)
print("O valor 2 passando pelo operador NOT retorna: ", not E2_bool)