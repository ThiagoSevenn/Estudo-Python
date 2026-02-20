# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
metros = float(input('Escreva um valor em metros para ser convertido: '))

centimetros = metros * 100
milimetros = centimetros * 10

print(f'\nO valor em metros foi de: {metros:.2f}\nEm centímetros é: {centimetros:.2f}\nEm milímetros é: {milimetros:.2f}')