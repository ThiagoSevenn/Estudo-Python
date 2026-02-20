# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados em: 
# unidade de milhar, centena, dezena, unidade

numero = input('Digite um número de 0 - 9999: ')

print('\nO número possui {} unidade(s) de milhar, {} centena(s), {} dezena(s), {} unidade(s).'.format(numero[0],numero[1],numero[2],numero[3]))