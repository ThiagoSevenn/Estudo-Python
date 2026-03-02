# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
print('Números pares:')
for numero in range(1,50):
    if numero%2 == 0:
        print('Número:',numero)