# Faça um programa que leia um número qualquer e mostre o seu fatorial.

decaimento = numero = int(input('Digite um número para descobrir seu fatorial: '))
fatorial = 1
while decaimento != 1:
    fatorial *= decaimento
    decaimento -= 1

print(f'\nO fatorial do número {numero} é {fatorial}')