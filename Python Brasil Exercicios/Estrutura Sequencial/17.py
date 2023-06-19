#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da 
#tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
tamanho = float(input ("Digite o tamanho em metros quadrados: "))
tamanho = tamanho*1.1
import math

if tamanho < (18 * 6):
    galoes = math.ceil(tamanho / (3.6 * 6))
    print (f"Será necessário: {galoes} galões de tinta. Total: R$ {galoes * 25}")    
else:
    latas = tamanho // (18 * 6)
    print(f"Será necessário: {latas} latas de tinta. Subtotal: R$ {latas*80}")
    galoes = math.ceil((tamanho - (latas * 18 * 6)) / (3.6 * 6))
    print(f"Será necessário: {galoes} galões de tinta. Subtotal: R$ {galoes*25}")