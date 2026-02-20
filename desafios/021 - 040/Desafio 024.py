# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
nome_cidade = input('Digite o nome de uma cidade: ')

print('\nO nome dessa cidade começa com a palavra "SANTO"? {}'.format(nome_cidade.upper().split(' ')[0] == 'SANTO'))