# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o preço de um produto: '))

reajuste = preco * 0.95

print(f'\nO novo preço do produto será de R${reajuste:.2f}')