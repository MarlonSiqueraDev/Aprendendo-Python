#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
tuplavogais = ('a','e','i','o','u')

letra = input("Digite a letra em minuscula: ")
if letra in tuplavogais:
    print("É uma vogal.")
else:
    print ("É uma consoante.")