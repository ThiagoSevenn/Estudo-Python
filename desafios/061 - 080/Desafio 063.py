# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

n = int(input('Digite um número de elementos da sequência de fibonacci:'))
fibonacci = 0
numero_um = numero_dois = 1
print(f'\n{f'SEQUÊNCIA DOS {n} PRIMEIROS TERMOS':-^40}',end='\n\nfib: ')
while n >= 1:
    n -= 1
    if n < 1:
        print(numero_um, end='\n')
    else:
        print(numero_um, end=' ')
    auxiliar = numero_um + numero_dois
    numero_um = numero_dois
    numero_dois = auxiliar
    
print(f'\n{'FIM':-^40}')