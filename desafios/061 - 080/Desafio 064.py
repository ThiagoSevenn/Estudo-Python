# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles( desconsiderando o flag)

quantidade_numeros = 0
soma = 0
numero = int(input('Digite um número inteiro: '))
while numero != 999:
    soma += numero
    quantidade_numeros += 1
    numero = int(input('Digite um número inteiro: '))

print(f'{'INFORMAÇÕES':-^30}')
print(
f'''
Total de números digitados: {quantidade_numeros}
Soma total: {soma}
''')
print(f'{'':-^30}')