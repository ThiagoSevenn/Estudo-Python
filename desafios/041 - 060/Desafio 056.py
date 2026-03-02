# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

media = 0
mais_velho_nome = ''
mais_velho = 0
mulheres_menor_vinte = 0
for i in range(0,4):
    nome = input(f'Digite o nome da {i + 1}ª pessoa: ')
    idade = int(input(f'Digite a idade da {i + 1}ª pessoa: '))
    sexo = input(f'Digite o sexo da {i + 1}ª pessoa: ')
    
    media += idade
    if idade > mais_velho:
        mais_velho = idade
        mais_velho_nome = nome
    
    if sexo == 'feminino' and idade < 20:
        mulheres_menor_vinte += 1
    
print(f'''\nDados analisados:
A média de idade do grupo é: {int(media/4)} anos.
{mais_velho_nome} é o nome do homem mais velho.
{mulheres_menor_vinte} mulheres têm menos de 20 anos.''')

    