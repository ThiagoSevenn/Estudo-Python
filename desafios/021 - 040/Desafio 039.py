# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento do jovem? '))

print()

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if(idade == 18):
    print('Está na hora de se alistar no serviço militar.')
elif(idade > 18):
    print('Passou do tempo de se alistar!')
else:
    print('Faltam {} anos para o jovem conseguir se alistar.'.format(18 - idade))