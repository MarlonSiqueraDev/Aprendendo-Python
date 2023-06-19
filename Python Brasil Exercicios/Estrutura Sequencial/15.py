#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

porhora = float(input("Digite o salário por hora: "))
horas = int(input("Digite quantas horas trabalhadas: "))

salariobruto = porhora*horas
inss = salariobruto * 8 / 100
sindicato = salariobruto * 5 / 100
ir = salariobruto * 11 / 100
descontos = inss + sindicato + ir
liquido = salariobruto - descontos

print ("Salário Bruto: ", salariobruto)
print ("INSS: ", inss)
print ("IR: ", ir)
print ("Sindicato: ", sindicato)
print ("Descontos: ", descontos)
print ("Salário Liquido: ", liquido)