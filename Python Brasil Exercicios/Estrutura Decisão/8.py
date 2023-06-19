#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o 1º Preço: "))
preco2 = float(input("Digite o 2º Preço: "))
preco3 = float(input("Digite o 3º Preço: "))

if preco1<preco2 and preco1<preco3:
    print("Comprar Preço 1: ", preco1)
elif preco2<preco3:
    print("Comprar Preço 2: ", preco2)
else:
    print("Comprar Preço 3: ", preco3)