#Questao01
'''
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
resultado = n2/n1
print (f'O resultado da divisão de {n2} por {n1} e {resultado:.2f} ')
'''
#Questão 02
'''
farh =float(input ("Digite um valor de Fahrenheit: "))
celsius = (farh-32)/1,8
print (f'O valor da convensão e igual a : {celsius}')
'''
#Questão 03
'''
dolar = float(input('Digite um valor em dolar: '))
real = dolar*5
print (f'o valor em reais e {real}')
'''
#Questão 04
'''
n1 = float(input("Digite o terceiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero:"))
media = (n1 + n2 + n3)/3
print (f'o resultado da media é {media}')
'''
#Questão 05
'''
nome = str(input("Digite o seu nome:"))
print (type(nome))
'''
#Questão 06
'''
lista_principal=[]
lista_dobro=[]
for _ in range(1,11):
    n = int(input('Digite numero para a lista:'))
    lista_principal.append(n)
    nd = n*2
    lista_dobro.append(nd)
print (f'Aqui esta os numeros que você escolheu{lista_principal}')
print (f'Aqui esta o dobro dos numeros que você escolheu{lista_dobro}')
'''
# Questão 07
'''
num1 = float(input("Me digaum número para a comparação: "))
num2 = float(input("Me diga um novo número para prosse com a comparação: "))
result = "num1 é maior if num1>num2 else "num1 é menor"
print (result)
'''
#Questão 08
nome1 = input("Digite o primeiro nome completo: ")
nome2 = input("Digite o segundo nome completo: ")
# separando o nome do sobrenome
parte1 = nome1.split ()
parte2 = nome2.split ()
#pegar o primeiro nome e sobrenome
primeiro_nome1 = parte1[0]
sobrenome1 = parte2[-1]
primeiro_nome2 = parte2[0]
sobrenome2 = parte1[-1]
novo_nome1 = primeiro_nome1 +""+ sobrenome2
novo_nome2 =primeiro_nome2 +""+ sobrenome1
print (novo_nome1)
print (novo_nome2)