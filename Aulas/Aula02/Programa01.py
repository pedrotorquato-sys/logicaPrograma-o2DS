"""
    Calculos e manipulação de variaveis
"""

nome = input ("Digite o seu nome: ")
idade = input ("digite a dus idade: ")
peso = input ("Digite a o seu peso: ")
altura = input ("Digite a sua altura: ")

# tratamento de exceção
try:
    idade = int (idade)
    peso = float (peso)
    altura = float (altura)
except ValueError as e:
    print (e)

imc = peso / altura **2
print ("seu imc é: ", imc)
