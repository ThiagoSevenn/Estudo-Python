# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0 
for numero in range(0,6):
    x = int(input('Digite um número inteiro: '))
    if x%2 == 0:
        soma += x

print('A soma de todos os números pares digitados foi de {}'.format(soma))