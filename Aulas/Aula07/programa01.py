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
carro= []
proximo_id = 1

while True:
    print('\n============= Sistema de Carros 🚗 =============')
    print('1 - Cadastrar Carros')
    print('2 - Listar Carros')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    os.system('cls')

    #create
    if opcao == '1':
        while True:
            modelo = input("Digite o modelo: ").title()
            preço = input("Digite o preço: ").title()
            marca = input("Digite o marca: ").title()
            carros = {
                "id"         : proximo_id,
                "modelo":modelo,
                "preço":preço,
                "marca":marca
            }
            with open("carros.txt",'a')as arquivo:
                arquivo.write(f"{modelo}")
                arquivo.write(f"{preço}")
                arquivo.write(f"{marca}\n")

            sair = input("Deseja sair?s/n").lower()

            if sair =='s':
                break    



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
            with open('carros.txt','r')as arquivo:
                for linhas in arquivo:
                    print(linhas.strip())  

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
        del carro[1:5]
        break

    else:
        print('❌ Opção inválida.')