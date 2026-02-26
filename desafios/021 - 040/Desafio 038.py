# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é o maior.
# O segundo valor é o maior.
# Não existe valor maior, os dois são iguais.

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

print()

if(primeiro_numero > segundo_numero):
    print('O primeiro número é o maior.')
elif(segundo_numero > primeiro_numero):
    print('O segundo número é o maior.')
else:
    print('Os dois lados são iguais.')