#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))
total = (hora*60)*60 + minuto*60 + segundo 
totalprint = "O total de segundos é: {} ".format(total)
print(totalprint)