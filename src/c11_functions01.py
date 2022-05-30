# > FUNÇÕES

# 1. o que são funções e por que utilizá-las?

# funções que já utilizamos anteriormente...
"""
print() # - imprime uma mensagem (int, float, str) no console (terminal, cmd)
input() # - retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - recebe uma lista e retorna o tamanho dessa lista
max() # - retorna o maior valor de uma lista
"""

# 2. criação de funções
# função inicial

def saudacao(): #criando função / def = define
    print('seja bem-vinda(o)!')
    print('olá, é um prazer ter voce fazendo parte desse curso')

saudacao() #uma funcao ao ser criada, deve ser chamada para ser executada (caixa preta = cria a estrutura = utiliza)
# sempre se coloca parenteses depois da função, ex print()
# uma vez definida, pode ser usada varias vezes

# função com parâmetros
def saudacao(nome, curso): # dentro dos parenteses colocamos os parametros
    print(f'seja bem-vinda(o)!', {nome})
    print(f'olá, é um prazer ter voce fazendo parte do curso de {curso}!')

saudacao('milena', 'java') #passamos o que queremos, recebe e joga o nome
saudacao('jailene', 'python')

# função com parâmetros default
def saudacao(nome, curso='python'): # dentro dos parenteses colocamos os parametros pré-definidos
    print(f'seja bem-vinda(o)!', {nome})
    print(f'olá, é um prazer ter voce fazendo parte do curso de {curso}!')

saudacao('milena', 'c++') #não é obrigatório passar para c++, mas se não mudar, irá assumir o valor padrão/ caso quisesse alterar o parâmetro pré-definido

# funções com retorno
# função é uma caixa preta com entrada, processamento e saída
# resultado de uma função é retorno

def soma(num1, num2):
    #print('Soma = ', num1 + num2)
    return num1 + num2 # sempre que utiliza o reeturn, a função para de executar. retorna a função e acaba. é recomendado usar no final da função
    #print('olá') não aparece pois está após o return

resultado = soma(5, 7)
print('o resultado da soma é ', resultado)

# para criar uma função que seja reutilizavel em diversos cenarios, é recomendado que nao imprima dentro da função, e sim retorne o conteudo que o usuario precise

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print(resultado)