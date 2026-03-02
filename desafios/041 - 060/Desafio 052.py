# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
divisores = 0
for x in range(1, numero+1):
    if numero%x == 0:
        divisores += 1
    
print(f'O {numero} é primo ' if divisores <= 2 else f'O {numero} não é primo')