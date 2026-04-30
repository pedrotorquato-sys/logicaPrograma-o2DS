'''
    Programa 01 - Aula04 - 28/04
    prof: karython
    Turma
'''

import os
import random

lista_nomes = ['Lucas Almeida',
'Mariana Souza',
'Rafael Pereira',
'Camila Rodrigues',
'Gustavo Ferreira',
'Fernanda Costa',
'Diego Martins',
'Juliana Oliveira',
'André Barbosa',
'Beatriz Ribeiro',
'Henrique Gomes',
'Larissa Carvalho',
'Vinícius Rocha',
'Patrícia Dias',
'Eduardo Teixeira',
'Aline Fernandes',
'Bruno Moreira',
'Renata Nunes',
'Felipe Cardoso',
'Natália Monteiro']
nome_sorteado = random.choice(lista_nomes)
lista_sorteados = []
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print (f'Sorteado:{nome_sorteado}')
    lista_sorteados.append(nome_sorteado)
    lista_nomes.remove(nome_sorteado) 
    sorteados +=1

print(' Fim do programa')