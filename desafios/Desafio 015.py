# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
# R$ 0.15 por Km rodado.
km_percorridos = float(input('Quantos km foram percorridos com o carro: '))
dias = int(input('Digite a quantidade de dias em que ele foi alugado: '))

preco_total = (dias * 60) + (km_percorridos * 0.15)

print(f'\nO preço total a ser pago pelo alugel é: R${preco_total:.2f}')