"""
    Siatema:calculadora
"""


while True:
    print(30*"-","Calculadora",30*"-")
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite o numero: '))
    print('1.soma')
    print('2.subtração')
    print('3.Multiplicão')
    print('4.Divisão')
    opção = input('Digite a operação: ')

    match opção:
        case '1':
            resultado = num1+ num2
            print (f'{num1}+{num2}={resultado}')
            break
        case '2':
            resultado = num1- num2
            print (f'{num1}-{num2}={resultado}')
            break
        case '3':
            resultado = num1* num2
            print (f'{num1}*{num2}={resultado}')
            break
        case '4':
            resultado = num1/ num2
            print (f'{num1}/{num2}={resultado}')
            break
        case '_':
            print("Digite um numero válido")
       