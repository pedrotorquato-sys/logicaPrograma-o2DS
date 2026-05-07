'''
    Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo
    passar o comando de abertura de arquivos, passar comando de ação

    arquivo = open('arquivo.txy','modo')

    modos de ação:
        - "r" : Leitura do arquivo
        - "w" : escrita(sobrescreve o contrudo antigo)
        - "a" : adicionar conteudo
        - "x" : criar um arquivo
        - "b" : arquivos binarios
        - "t" : texto 
'''
# Criando e escrever arquivo
arquivo = open ('primeiro_arquivo.txt',"w")
arquivo.write('ola mundo! meu primeiro arquivo')
arquivo.close()

# Lendo arquivo
arquivo = open("primeiro_arquivo.txt","r")
conteudo = arquivo.read()
print (conteudo)
arquivo.close()

#aplicando boa pratica
with open ("primeiro_arquivo.txt","r")as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#arquivo com multiplas escritas
with open('alunos.txt','w') as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('João\n')
    arquivo.write('Lucas\n')
    arquivo.write('Gomes\n')
    arquivo.write('Karython\n')

#Lendo linha a linha
with open('alunos.txt', 'r')as arquivo:
    for linha in arquivo:
        print (linha)

#usar lista para escrevar no arquivo
frutas = ['pera','abacaxi','melancia','manga','caju']

with open ('frutas.txt','w')as arquivo:
    for f in frutas :
        arquivo.write(f+'\n')

# converter o arquivo em uma lista
with open('frutas.txt','r')as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)

# Saida: ['pera\n]

#limpar a quebra de linha

with open('frutas.txt','r')as arquivo:
    for linhas in arquivo:
        print(linhas.strip())


#Exemplo para cadastro

while True:
    nome = input("Digite o seu nome: ").title()

    with open("cadastro.txt",'a')as arquivo:
        arquivo.write(nome+"\n")

    sair = input("Deseja sair?s/n").lower()

    if sair =='s':
        break