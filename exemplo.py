lista = ['henry', 'laura', 'natha']
print(lista)
#listas podem mudar e ser modificadas
ultimo_item = lista.pop()
print('o último item da lista é', ultimo_item)
print(lista)

#tuplas não podem ser modificadas -> para retirar ou add novos "atributos",deve-se criar uma nova tupla
tupla = ('henry', 'laura')
print(tupla)
print(tupla[0])

#sets ou conjuntos -> semelhante aos conjuntos numéricos
A = {'henry', 'laura'}
B = {'henry', 'natha'}

print('conjunto A:', A)
print('conjunto B:', B)
print('interseção: ', A.intersection(B))
print('união: ', A.union(B))
print('A - B: ', A - B)
print('B - A: ', B - A)

#dicionario -> relação chave para valor
dic = {'henry': 32, 'laura': 16, 'natha': 32}
rev = {32: ['henry', 'natha'], 16: 'laura', 8: {'pedro': 8.5, 'joão': 8.9}}

print('dicionário como ele é:', dic)
print('o valor na chave henry é', dic['henry'])
print(rev[32])
print('todos as chaves:', list(dic.keys()))
print('todos os valores:', list(dic.values()))

for chave, valor in dic.items():
    print(chave, valor) #"listar" por dupla chave-valor
