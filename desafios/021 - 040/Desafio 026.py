# Faça um programa que leia uma frase e mostre:
# ~> Quantas vezes aparece a letra 'A'.
# ~> Em que posição ela aparece a primeira vez.
# ~> Em que posição ela aparece a última vez.

# Frase exemplo será: A sabedoria é uma dádiva.
# 5 letras "A"
# Primeira aparição: 0
# Última aparição: 23

frase = input('Digite uma frase: ')

print('''\nSua frase: {}
A letra "A" aparece: {}
Aparece a primeira vez na posição: {}
Aparece a última vez na posição: {}'''.format(frase,frase.upper().count('A'),frase.upper().find('A'),frase.upper().rfind('A')))


