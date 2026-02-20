# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians ,sin, cos, tan

angulo = float(input('Digite um ângulo(em graus) que deseja saber seu seno, cosseno e tangente: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nO valor do ângulo: {angulo}°\nSeu seno: {seno:.2f}\nSeu cosseno: {cosseno:.2f}\nSeu tangente: {tangente:.2f}')