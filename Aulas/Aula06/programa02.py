'''
    Dsenvolva um sistema de gerenciamento de Carros dom realização do CRUDS
'''

import os
import time
carros = []
proximo_id = 1

os.system('cls')
while True:
    print ("\n====== Sistema de carros 🚗 ======")
    print ('1 - Cadastre carro')
    print ('2 - Liste carros')
    print ('3 - Atualizar carro')
    print ('4 - Deletar carro')
    print ('0 - Sair')

    opcao = input ('Escolha uma opcao: ')

    #criar
    if opcao == '1':
        modelo = input ('Digite o modelo do carro: ').title()
        preco = float (input ("Digite o preço: "))
        marca = input("Digite a marca do carro: ")
        
        carro = {
            'id': proximo_id,
            'modelo':modelo,
            'preço': preco,
            'marca': marca
        }

        carros.append(carros)
        proximo_id+1

        print ('✅Carro cadastrado com suceso')
    #read
    elif opcao == '2':
        if not carros:
            print ('❌Nenhum carro enconteado')
        else:
            print ('\n📋Lista de carro ')
            for carro in carros:
                print (f'ID: {carro['id']}| Modelo:{carro['modelo']}|Preço:{carro['preço']}|Marca:{carro['marca']}')
    #update
    elif opcao == '3':
        print ('\n Lista de carros')
        print (f'ID: {carro['id']}|Modelo: {carro['modelo']}|Preço: {carro[preco]}|Marca{carro['marca']}')
        id_buscar= int(input('Digiteo id do carro para atualizar'))

        encontrado = False
        for carroo in carros:
            if carro['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco= float(input('Digite o novo preço: ')).replace(',','.')
                nova_marca= input('Digite a nova marca:').title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                prin('✅ Carro atualizado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('❌ Carro não encontrado!')
    #delete
    elif opcao =='4':
        print ('\n Lista de carros')
        print (f'ID: {carro['id']}|Modelo: {carro['modelo']}|Preço: {carro[preco]}|Marca{carro['marca']}')
        id_buscar= int(input('Digiteo id do carro para deletar'))

        encontrado = False

        for carroo in carros:
            if carro['id'] == id_busca:
                carros.remote(carro)
                print('✅ Carro deletado com sucesso!')
                encontrado = True
                break

    #Sair
    elif opcao =='0':
        print ('Saindo do sistema...')
        total = 20
        for i in range(total +1):
            porcentagem = int((i/total)*100)
            barra +="🟩"
            vazio = "-" * (total+1)
            print(f'\r[{barra}]{porcentagem}%', end="")
            time.sleeo(0.3)
        break
    else:
        print ('Opcao invalida.')
            