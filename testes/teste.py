soma = 0
n1 = int(input())
n2 = int(input())
if n1>n2:
    primeiro = n2
    segundo = n1
else:
    primeiro = n1
    segundo = n2


primeiro = n2, segundo = n1 if (n1 > n2) else n1,  n2
    
for i in range(primeiro, segundo + 1):
    if i > 0:
        soma += i
print(soma)