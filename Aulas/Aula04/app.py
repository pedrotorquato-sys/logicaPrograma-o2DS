# for

#laço de for, ele é finito quando eu sei o numero de repetição
#frutas = ['melancia','abacaxi','melão','pera']
#fruta = 'melacia'
#for f in fruta:
#    print (f)

#for range(inicio, fim, salvo)

#for _ in range(1,20,2):
  #  print("Repeti")
'''
num = int(input('Digite um numero para saber a sua tabuada:'))

for i in range(1,11):
    print(f"{i} X {num} = {i * num}")
    '''



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

for i,nome in enumerate(lista_nomes):
    print(i+1,'º',nome)

    nome_buscar = input("Digite um numero para buscar").title()

if nome_buscar in lista_nomes:
    print ('Usuario encontrado!')