# Formatação de string
## '\n' serve para pular uma linha.
print('{:_^40}'.format('Formatação string'))

string = 'Olá, mundo!!'
str = 'Olá,', ' mundo!!'
str1 = 'Olá,' + ' mundo!!'

mundo = 'mundo!!'
str2 = 'Olá, {}'.format(mundo)
str3 = f'Olá, {mundo}'

print(string)
print(str)
print(str1)
print(str2)
print(str3)

print('_'*30)

nome = input("Digite seu nome: ")

# Nome vai ser escrito em 20 caracteres, seria representado somente po '{:20}'

## Nome vai ser escrito formatando a esquerda '<'.
print('Seu nome é {:<20}, Prazer!!'.format(nome))
## Nome vai ser escrito formatando centralizado '^'.
print('Seu nome é {:^20}, Prazer!!'.format(nome))
## Nome vai ser escrito formatando a direita '>'.
print('Seu nome é {:>20}, Prazer!!'.format(nome))
## Nome vai ser escrito formatando a direita '>' e nos espaços que seriam ' ', escolhi o caracter '-' para substituir.
print('Seu nome é {:->20}, Prazer!!'.format(nome))

# A função print tem por padrão uma quebra de linha, 
# para mudar isso, utilizasse ', end=', após o '=' escolhe a string que aparecerá ao final do print.
print('Por padrão ele pula a linha')
print('Sem seguir esse padrão e exigindo que ele finalize com um "terminei." ', end='terminei.')

print('\n')

print('{:_^40}'.format('Formatação Float'))

# Formatação de tipo Float
numero = 1.333333333

print(f'O número é: {numero}')
print(f'O número é (2 casa decimais): {numero:.2f}')
print('O número é (4 casas decimais): {:.4f}'.format(numero))