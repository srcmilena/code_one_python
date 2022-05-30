# lists structure

# before
grade1 = 7.9
grade2 = 9.7
grade3 = 8.2

# with array
grades = [7.9, 9.7, 8.2]

# creating arrays (both below are empty list)
list = []
#list = list()

# lists in py allow different types of data (int + str + float + boolean...)
list = [26, 'milena', 3.14159, False]

# array inside array
list_of_list = [10, [1, 2, 3]]

# indexing and slices (slicing)
list = [10, 'milena', 3.1415, True]

print(list[0]) #acessando um elemento
print(list[1])
print(list[2])
print(list[3])
# print(list[4]) #does not exist, error
print(list[-1]) # -1 = last item; -2 penultimo... pode indexar com valores negativos e positivos

# slices (pedaços da lista) - indexação
list = [10, 50, 30, 40, 25, 60, 5]
print(list[0:3]) #querendo pegar os elementos 1 e 2, porém, com esse comando, começa do 0 e vai até o -3 (indice)
print(list[3:6])
print(list[3:]) #caso eu não queira que tenha um final dos elementos
print(list[2:6:2]) #vai do 2 ate o 6 pulando de 2 em dois (em termos de posição)

# > iterações com for
# 1. utilizando os próprios elementos da lista
for elemento in list: #vai a cada iteração passar por cada um dos elementos na lista
    print(elemento)

# 2. utilizando os indices
print('o comprimento da lista: ', len(list)) #len = length/ quantidade de elementos dentro da losta

for i in range(len(list)):
    print(i) #vai imprimir os indices, que serao de 0 a 6 numa lista de 7 elementos
    print(list[i]) #vai acessar cada elemento e vai imprimir de acordo com o indice