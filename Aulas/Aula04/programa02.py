import random
import os
import time

lista_nomes =[]
lista_sorteado = []

print (30*"-","Bem vindo ao sistema de sorteios")

while True :
    nome = input ("Digite um nome para ser sorteado: ").title()
    lista_nomes.append(nome)
    opção = input ("Deseja adicionar mais? (S - Sim) ou enter pata parar!")

    if opção!= "S":
        break

while True:
    if not lista_nomes:
        print('A lista de nomes está vazia!')
        break
    else:
        nome_sorteado=random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteado.append(nome_sorteado)
        os.system('cls')

    for i in range(5,0,-1):
        time.sleep(1)
        os.system('cls')
        print(f'Contagem regressiva...{i}')

    print (f'O sorteador foi: {nome_sorteado}')
    sortear_novamente = input ('Deseja sortear outro nome?')
    if sortear_novamente =='n':
        break
print (lista_sorteado)
print ('Fim do programa')