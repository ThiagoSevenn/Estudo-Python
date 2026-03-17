# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.
from random import randint

print(f'{'PROGRAMA':-^40}')
numeros_aleatorios = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior = menor = numeros_aleatorios[0]

for numero in numeros_aleatorios:
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero

print('Os números gerados aleatoriamente foram: {}'.format(numeros_aleatorios))
print('O maior entre os números: {}\nO menor entre os números: {}'.format(maior,menor))
print(f'{'FIM':-^40}')

