# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
for numero in range(1,500):
    if (numero%3 == 0 and numero%2 == 1):
        soma += numero

print('A soma total de todos os números ímpares que são múltiplos de três:', soma)