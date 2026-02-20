# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = input('Digite seu nome completo: ')

print(f'\nO seu nome completo tem "SILVA"? {nome.upper().__contains__('SILVA')}')