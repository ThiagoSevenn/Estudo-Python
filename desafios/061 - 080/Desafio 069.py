# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. Ao final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$ 1000
# Qual o nome do produto mais barato.

print('{:-^40}'.format('REALIZAR COMPRA'))

total_gasto = produtos_mais_mil = mais_barato = 0
nome_mais_barato = ''
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    
    total_gasto += preco
    
    if preco > 1000:
        produtos_mais_mil += 1
        
    if mais_barato == 0:
        mais_barato = preco
    elif mais_barato > preco:
        mais_barato = preco
        nome_mais_barato = nome       
    
    continuar = input('Deseja continuar?(s/n) ')
    print()
    if continuar == 'n':
        break
    
print('{:-^40}'.format('RESUMO DA COMPRA'))
print('Total gasto na compra: R${:.2f}'.format(total_gasto))
print('Produto mais barato da lista: {} por {:.2f}'.format(nome_mais_barato, mais_barato))
print('Produtos que custam mais de R$ 1000,00: {}'.format(produtos_mais_mil))
print('{:-^40}'.format('COMPRA FINALIZADA'))