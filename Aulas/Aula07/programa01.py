'''
    Desenvolva um sistema de gerenciamento de veiculos, permitindo cadastrar
    o veiculo pegando do uduario os seguintes dados (modelo,marca,preço)

    -os dados devem ser armazenados em um arquivo.
    -o usuario deve poder cadastrar quantos carros quiser sem ter que
        rodar o sistema  novato.
    -deve ter a opção de ler os carros existentes
    -devem ser cadastrados em um arquivo .json e usar dicionario
'''
import os
import time

carros = []
proximo_id = 1

os.system('cls')
while True:
    print('\n============= Sistema de Carros 🚗 =============')
    print('1 - Cadastrar Carros')
    print('2 - Listar Carros')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    os.system('cls')

    #create
    if opcao == '1':
        modelo = input('Digite o modelo do carro: ').title()
        preco = float(input('Digite o preço: '))
        marca = input('Digite a marca: ').title()

        carros = {
            "id"         : proximo_id,
        }
        with open('infor_carros.txt','w') as arquivo:
            arquivo.write(f'{modelo}\n')
            arquivo.write(f'{preco}\n')
            arquivo.write(f'{marca}\n')


        proximo_id += 1

        print('✅ Carro Cadastrado com sucesso!')

        time.sleep(3)
        os.system('cls')

    #read
    elif opcao == '2':
        if not carros:
            print('❗Nenhum carro cadastrado.')
        else:
            print('\n 📋 Lista de carros')
            with open('infor_carros.txt','r')as arquivo:
                linhas = arquivo.readlines()

                print(type(linhas))
                print(linhas)    

    #Sair
    elif opcao == '0':
        total = 20
        barra =""
        print('Saindo do Sistema...')
        for i in range(1, total +1):
            barra +="🟩"
            porcentagem = int((i / total *100))
            vazio = "-" * (total -1)
            print(f'\r[{barra}] {porcentagem}%', end="")
            time.sleep(0.2)
        break

    else:
        print('❌ Opção inválida.')