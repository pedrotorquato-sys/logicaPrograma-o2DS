import modulo as ma

if __name__ == "__main__" :
    while True :
        print ("Calculadora")
        print ("1.Soma")
        print ("2.Suntrair")
        print ("3.Multiplicar")
        print ("4.Dividir")
        print ("5.Limpar terminal")
        opcao = input('Digite a opção desejada')
        match opcao:
            case '1':
                print('-----SOMA-----')
                num1 = int(input('Digite um número para somar: '))
                num2 = int(input('Digite outro número para somar: '))
                result = ma.soma(num1,num2)
                print(f'Resultado:{result}')
                break
            case '2':
                print('-----Subtrair-----')
                num1 = int(input('Digite um número para subtrair: '))
                num2 = int(input('Digite outro número para subtrair: '))
                result= ma.sub(num1,num2)
                print (f'Resultado:{result}')
                break
            case '3':
                print('-----MULTIPLICAR-----')
                num1 = int(input('Digite um número para multiplicar: '))
                num2 = int(input('Digite outro número para multiplicar: '))
                result= ma.mult(num1,num2)
                print (f'Resultado:{result}')
                break
            case '4':
                print('-----DIVIDIR-----')
                num1 = int(input('Digite um número para dividir: '))
                num2 = int(input('Digite outro número para dividir: '))
                result= ma.div(num1,num2)
                print (f'Resultado:{result}')
                break
            case '5':
                ma.limpar_terminal()
                break
            
            case _:
                print("Opção inválida!")