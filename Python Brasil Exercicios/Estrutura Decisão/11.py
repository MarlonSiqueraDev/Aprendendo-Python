#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_atual = float(input("Digite o salário atual: "))
salario_novo = 0
percentual = 0
if salario_atual<= 280:
    salario_novo = salario_atual*1.20
    percentual = 20
elif salario_atual<=700:
    salario_novo = salario_atual*1.15
    percentual = 15
elif salario_atual<=1500:
    salario_novo = salario_atual*1.10
    percentual = 10
else:
    salario_novo = salario_atual*1.05
    percentual = 5

print("Salario atual: ",salario_atual)
print("Percentual de aumento: ",percentual)
print("Valor do aumento: ",salario_novo-salario_atual)
print("Salario Reajustado: ",salario_novo)