# Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza 
# Primeiro = Ana
# Último = Souza

nome_completo = input('Digite o nome ocmpleto de uma pessoa: ')

print(f'\nNome completo: {nome_completo}\nPrimeiro nome: {nome_completo.split(' ')[0]}\nÚltimo nome: {nome_completo.split(' ')[len(nome_completo.split(' ')) - 1]}')