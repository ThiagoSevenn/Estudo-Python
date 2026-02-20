# Crie um programa que leia um número inteiro e mostre na tela se ele é impar ou par.

numero = int(input('Digite um número para saber se ele é par ou ímpar: '))

print(f'{numero} é par.' if(numero % 2 == 0) else f'{numero} é ímpar.')