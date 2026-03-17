# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print(f'{'PROGRAMA':-^40}')
valor_um = int(input('Digite um valor: '))
valor_dois = int(input('Digite um valor: '))
valor_tres = int(input('Digite um valor: '))
valor_quatro = int(input('Digite um valor: '))

tupla_valores = (valor_um,valor_dois,valor_tres,valor_quatro)

pares = ''
posicao_tres = tupla_valores.index(3)
contador_nove = 0
for valor in tupla_valores:
    if valor == 9:
        contador_nove += 1
    if valor % 2 == 0:
        pares += f'{valor} '

print(f'''\nA tupla {tupla_valores} apresenta:
O valor 9 apareceu {contador_nove} vezes.
O primeiro valor 3 apareceu no index {posicao_tres}.
Os números pares são: {pares}''')

print(f'{'FIM':-^40}')