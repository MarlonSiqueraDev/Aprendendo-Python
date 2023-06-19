#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o 
#tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input("Digite o tamanho do arquivo (MB): "))
link = int(input("Digite a velocidade da internet (Mbps): "))

minutos = (tamanho/link)//60
segundos = (tamanho/link)%60

print(f"Tempo estimado: {minutos} minutos e {segundos} segundos.")