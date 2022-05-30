#> métodos de listas
# método é uma função que está atrelada a uma váriavel, sem entrar no escopo de orientação a objeto

list = [1, 3, 12, 6, 2]

# append = add um elemento no final da array
print('antes do append: ', list)
list.append(3)
print('depois do append: ', list)

# insert = add e escolhemos a posição de onde queremos add pelo indice
print('antes do insert: ', list)
list.insert(2, 10) #primeiro a posicao(2), depois o valor(10)
print('depois do insert: ', list)

# extend = add um array em outra array

list2 = [1, 2, 3]
list.extend(list2)
print('depois do extend: ', list)

# pop = remove o elmento que especificar e se não especificar, remove o ultimo
list.pop()
print('lista após o pop: ', list)

list.pop(0)
print('lista após o pop: ', list)

# remove = diz qual valor (não o  indice) que queremos tirar e ele vai remover o primeiro valor que ele ver na lista

list.remove(3)
print('depois do remove: ', list)

# count = quantas vezs o elemeneto aparece nalista
print('quantidade de 2 na lista: ', list.count(2))

# index = indice de um determinado elemento/valor na lista
print('indice do elemento 12: ', list.index(12))

# sort = ordenar a lista
list.sort() #crescennt
print(list)

list.sort(reverse=True) #decrescent
print(list)
