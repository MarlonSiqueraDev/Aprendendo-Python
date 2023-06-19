#Tendo como dado de entrada a altura (h) de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input("Digite o sexo (F/M): ")
h = float(input("Digite a altura: "))

if sexo == "F":
    pesoideal = (62.1*h) - 44.7
    print ("Peso ideal: ", pesoideal)
elif sexo == "M":
    pesoideal = (72.7*h) - 58
    print ("Peso ideal: ", pesoideal)
else:
    print ("Sexo não informado corretamente.")