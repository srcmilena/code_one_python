# for = estrutura para  repetir de forma controlada, sabendo quantas vezes irá se rpeetir
# variavel acumuladora
sum = 0 #começa em zero pois é o elemento zero

for i in range(1, 4):
    grade = float(input(f'type your grade {i}: ')) # esse f na frente permite que adicione a variavel dentro da string dentro das chaves (variavel i injetada dentro da string), automatizando

    sum = sum + grade

    print(sum/3)
