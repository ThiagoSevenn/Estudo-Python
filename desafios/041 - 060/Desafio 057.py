# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = 'M'
while sexo == 'M' or sexo == 'F':
    sexo = input('Digite um sexo(F/M): ').upper()
    
print('\nValor incorreto informado.')