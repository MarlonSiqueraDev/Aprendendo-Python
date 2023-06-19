#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1 o produto do dobro do primeiro com metade do segundo .
#2 a soma do triplo do primeiro com o terceiro.
#3 o terceiro elevado ao cubo.

n1 = int(input("Digite o 1º numero inteiro: "))
n2 = int(input("Digite o 2º numero inteiro: "))
n3 = float(input("Digite o numero real: "))

resultado = (2 * n1) + (n2 / 2)
print ("1 - ", resultado)

resultado = (3 * n1) + n3
print ("2 - ", resultado)

resultado = n3 ** 3
print ("3 - ", resultado)