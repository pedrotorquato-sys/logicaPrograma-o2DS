# Note: Boletim Escolar 2.0

import os

os.system("cls")

print("Boletim Escolar")
lista_notas = []
nome = input ("Digite o nome do aluno: ").title()
curso = input ("Digute o curso: ").upper()

while True: 
    notas = input ("Digite uma nota: ")
    notas = float(notas)
    lista_notas.append
    print(lista_notas)

    opcao = input("Deseja adcionar mais notas? (enter - continue | n - Não)").lower()

    if opcao == "n":
        break
    
media = sum(lista_notas) / len(lista_notas)

print (media)