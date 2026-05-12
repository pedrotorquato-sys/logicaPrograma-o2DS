#função com parametro
'''def funcao_segundo_grau(a,b,c):
    return a,b,c

#chamando a função e armazenando o valor em uma variavel
x =  funcao_segundo_grau(1,2,3)
print(x)'''

'''def soma(a,b):
    resultado = a+b
    return resultado

num1= int(input("Digite um numero qualquer: "))
num2= int(input("Digite um numero qualquer: "))

resultado= soma(num1,num2)
print (resultado)'''

def mostrar_msg():
    print ('Olá mundo das funções!')

mostrar_msg()

def mostrar_saudacao(nome):
    print (f'Olá {nome}, seja bem-vindo!')

nome= input('Digite o seu nome: ')
mostrar_saudacao(nome)

#função recursiva
def fatorial(n):
    #n!
    return 1 if n == 0 else n * fatorial(n-1)

#função lambda
import os
somar = lambda x,y:x+y
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

#algoritmo principal
if __name__ == "__main__":
    try:
        x= int(input("Informe o valor de x: "))
        y= int(input("Informe o valor de y: "))
        result = somar (x,y)

        limpar()
        print(f"O resultado da soma é {result}.")
    except Exception as e:
        print (f"Não foi posível sonar.{e}.")