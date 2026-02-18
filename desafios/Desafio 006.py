# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))

print('\nO número digitado foi: {}\nO dobro do número digitado é: {}\nO triplo é: {}\nA raiz quadrada é: {:.1f}'
      .format(numero, (numero * 2), (numero * 3), (numero ** 0.5)))