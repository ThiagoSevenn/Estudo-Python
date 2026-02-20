# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distância de uma viagem em km: '))

preco_da_viagem = 0.5 * distancia if distancia <= 200 else 0.45 * distancia

print('O preço da passagem será R${:.2f}'.format(preco_da_viagem))