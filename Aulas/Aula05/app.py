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
lista_principal=[]
lista_dobro=[]
for _ in range(1,11):
    n = int(input('Digite numero para a lista:'))
    lista_principal.append(n)
    nd = n*2
    lista_dobro.append(nd)
print (f'Aqui esta os numeros que você escolheu{lista_principal}')
print (f'Aqui esta o dobro dos numeros que você escolheu{lista_dobro}')