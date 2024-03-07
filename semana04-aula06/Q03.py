# Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operacao = input("Digite ume operação: '+, -, *, /':")
match operacao:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 + num2)
    case "*":
        print(num1 + num2)
    case "/":
        print(num1 + num2)
