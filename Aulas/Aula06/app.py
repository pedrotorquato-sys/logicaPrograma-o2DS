'''
[] -> Lista/ Arey
{} -> Dicionario/ Objrto
() -> Tupla/ Const
'''
lista = ['gomes','fuano','joao','cicrano']
print (lista)

#imprimir valor especifico da lista
print (lista[0])
#imprimir ultimo indice
print (lista[-1])
#imprimir intervalo
print (lista[2:4])
#ordenar essa lista
#lista.sort()
#Adicinar na lista
lista.append ('Karython')
# incerindo em posição especifica
lista.insert(2,"Joao")
# incerindo varios valores
lista.extend(['ana','beatriz','david','roberto'])

numeros=[]

for i in range(10):
    numeros.append(i*2)
print(numeros)

#removendo item da lista
print (f'Lista antes de rmover {lista}')
#pop - remove pelo indice
lista.pop(0)

# removendo  o ulatimo
lista.pop()

#removendo pelo valor, (remove a primeira ocorrencia)
lista.remove ('citrano')

lista_numeros = [n for n in range (11)]
print (f'Lista antes de remover {lista_numeros}')
#removendo intervalo de valores
del lista_numeros[2:4]

print (f'Lista depois de remover {lista_numeros}')

listanomes = ['gomes','fuano','joao','cicrano','beltrano','maria','pedro']
#alteracao de valores da lista
listanomes[1] = 'lucas'

print (listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros [i] > 5:
        numeros[i] = numeros[i]*2
print (numeros)
numeros2 = [10,20,30,40,50]

#list compreheision
numeros = [n*2 if n>20 else n for n in numeros]
print (numeros)