# Conhecido como "laço", é utilizado para repetir x vezes tais linhas de código. Essas linhas de código podem ser
# qualquer coisa, de um atribuição de variável até um simples print.

# Existem algumas formas de desenvolver esses laços, sendo eles utilizando a estrutura "for" e/ou "While",
# serão apresentados a seguir. 

## Estrutura "for"

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

