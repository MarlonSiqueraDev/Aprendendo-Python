#Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = [0,0,0]
lista[0] = float(input("Digite o 1º numero: "))
lista[1] = float(input("Digite o 2º numero: "))
lista[2] = float(input("Digite o 3º numero: "))

lista.sort(reverse=True)
print(lista)