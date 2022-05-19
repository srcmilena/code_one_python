# chave = label - palavra / valor - significado da palavra

# definimos uma palavra para associar a um valor

# dicionarios

# criando dicionarios
dicionario = {} # definindo dicionario vazio
dicionario = dict()

dicionario = { 'nome': 'milena', 'idade': 5, 'altura': 1.77 } # primeiro definir uma chave e depois o valor

print(dicionario)
print(dicionario['idade']) #acessando elementos = colchetes + chave/label

# adicionando elementos em um dicionario
dicionario['programadora'] = True

print(dicionario)

dicionario['altura'] = 2 # vai sobreescrever o valor

print(dicionario)

# iterando sobre um dicionario

for chave in dicionario: #percorre as chaves a cada iteração
    print(chave, dicionario[chave])   # se acessamos a posição das chaves no dicionario, teremos o valor

# testando a exitência de uma chave
print('peso' in dicionario) #false
print('altura' in dicionario) # true
