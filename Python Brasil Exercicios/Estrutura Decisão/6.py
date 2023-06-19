#Faça um Programa que leia três números e mostre o maior deles.
n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))

if n1>n2 and n1>n3:
    print(n1)
elif n2>n3:
    print(n2)
else:
    print(n3)