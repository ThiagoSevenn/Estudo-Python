# Crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira.
from math import trunc

numero = float(input('Digite um número real qualquer: '))

print(f'\nO número é: {numero}\nSua porção inteira é: {trunc(numero)}')