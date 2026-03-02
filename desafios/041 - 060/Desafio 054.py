# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não antingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year

maioridade = 0
for i in range(0,7):
    idade = ano_atual - int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))
    if idade >= 18:
        maioridade += 1
        
print(f'\n{7-maioridade} é o total de pessoas que não são de maior.')