#Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch﻿ Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))

eAno = 31556926
eMes = 2629743
eDia = 86400

anoE = (ano - 1970) * eAno
mesE = (mes-1) * eMes
diaE = (eDia*dia)

data = (anoE + mesE + diaE)
print(data)

#1708387200
#1708431747