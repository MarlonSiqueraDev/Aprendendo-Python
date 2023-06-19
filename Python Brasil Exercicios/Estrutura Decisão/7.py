#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))

if n1>n2 and n1>n3:
    print("Maior: ", n1)
elif n2>n3:
    print("Maior: ", n2)
else:
    print("Maior: ", n3)

if n1<n2 and n1<n3:
    print("Menor: ", n1)
elif n2<n3:
    print("Menor: ", n2)
else:
    print("Menor: ", n3)