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
    print('olá, é um prazer ter voce fazendo parte do curso de {curso}!')

saudacao('milena', 'java') #passamos o que queremos, recebe e joga o nome
saudacao('jailene', 'python' )

# função com parâmetros default

