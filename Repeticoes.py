# Conhecido como "laço", é utilizado para repetir x vezes tais linhas de código. Essas linhas de código podem ser
# qualquer coisa, de um atribuição de variável até um simples print.

# Existem algumas formas de desenvolver esses laços, sendo eles utilizando a estrutura "for" e/ou "While",
# serão apresentados a seguir. 

## Estrutura "for" conhecida como 'Estrutura de repetição com variável de controle'
print(f'----{'Estrutura "For"': ^20}----\n')
## "Para cada i no intervalo(0,10), faça:"
print('Laço "For" convencional sem iteração definida.')
for i in range(0,10):
    print('Estou na numeração: ',i)

print()
## "Para cada i no intervalo(10,0,-1), faça:"
## Esse -1 atuará iterando o número 10 até chegar a 0, sem incluir o 0.
print('Laço "For" convencional com iteração definida.')
for i in range(10,0,-1):
    print('Estou na numeração: ',i)

print('-'*30 + '\n')


## Estrutura "while" conhecido como 'Estrutura de repetição com teste lógico'
print(f'----{'Estrutura "While"': ^20}----\n')

## "Enquanto i for menor que 10 faça:"
i = 0
while i < 10:
    print('Estou na numeração: ',i)
    i += 1

print()
    
## Existe uma preferência em utilizar o While quando não se tem certeza da quantidade de repetições que serão necessárias. Por exemplo:
numero_desconhecido = 0
while numero_desconhecido != 10:
    numero_desconhecido = int(input('Digite um número inteiro: '))
    print('Esse número não é conhecido.' if numero_desconhecido != 10 else 'Esse número é conhecido, parando o while.')

print('-'*30 + '\n')


 