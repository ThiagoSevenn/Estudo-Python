# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(0,5):
    peso = float(input('Digite o peso da {}ª: '.format(i + 1)))
    if maior < peso:
        maior = peso
    if menor > peso or i == 0:
        menor = peso

print(f'\nA pessoa de maior peso tinha {maior}Kg\nA pessoa de menor peso tinha {menor}Kg')