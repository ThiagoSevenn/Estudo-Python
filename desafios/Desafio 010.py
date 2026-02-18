# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 
# Cotação (ATUAL): 1 USD => 5,24 BRL 
dinheiro = float(input('Digite a quantia de reais que deseja converter para dólares: '))

print('\nCom a quantia de {:.2f} reais você conseguirá {:.2f} dólares.'.format(dinheiro,(dinheiro / 5.24)))