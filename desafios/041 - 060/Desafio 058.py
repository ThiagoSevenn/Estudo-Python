# Melhore o jogo do "Desafio 028" onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

jogador = 0
computador = 1
palpites = 0
while computador != jogador:
    computador = randint(0,10)
    jogador = int(input('Descubra qual foi o número(0 a 10) que a máquina escolheu: '))
    palpites += 1
    print('{:-^20}'.format(f'RODADA {palpites}'))
    print('Escolhas:\nmáquina: {}\nvocê: {}'.format(computador,jogador))
    print('-'*20)

print(f'Você demorou {palpites} jogadas para acertar qual foi o número escolhido pela máquina!')
