# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá dizer se o usuário perdeu ou venceu.
from random import randint

numero_predito = randint(0,5)

numero = int(input('Descubra qual foi o número(0 a 5) que a máquina escolheu: '))

print('Você venceu!!=)' if numero_predito == numero else 'Você perdeu! =(')
