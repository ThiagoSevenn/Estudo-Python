# Crie um programa que leia o nome completo de uma pessoa e mostre:
# ~> O nome com todas as letras maiúsculas
# ~> O nome com todas as letras minúsculas
# ~> Quantas letras ao todo (sem considerar os espaços)
# ~> Quantas letras tem o primeiro nome

nome_completo = input('Digite seu nome completo: ')

print(f'''\nO nome é: {nome_completo}
O nome em maiúsculas: {nome_completo.upper()}
O nome em minúsculas: {nome_completo.lower()}
Quantidade de letras ao todo: {len(nome_completo.replace(' ', ''))}
Quantidade de letras no primeiro nome: {len(nome_completo.split(' ')[0])}''')