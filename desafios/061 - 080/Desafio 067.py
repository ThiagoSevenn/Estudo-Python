# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint

vitorias = derrotas = 0
while True:
    print(f'{'ÍMPAR/PAR':-^60}')
    print(
'''
Você escolhe ímpar ou par(escreva impar/par)? ''',end='')
    escolha = input().lower()
    jogador = int(input('Digite um número: '))
    computador = randint(0,10)
    if escolha == 'par':
        if (jogador + computador) % 2 == 0:
            vitorias += 1
        else: 
            derrotas += 1
    else:
        if (jogador + computador) % 2 == 1:
            vitorias += 1
        else: 
            derrotas += 1
        
    print(f'{'-':-^60}')
    if derrotas > 0:
        break

print(f'Você venceu {vitorias} veze(s)!!')