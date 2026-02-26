# Crie um programa que faça o computador jogar jokenpô com você.
from random import choice

escolha_usuario = input('Escolha entre pedra, papel e tesoura: ').lower()

escolha_computador = choice(('pedra','papel','tesoura'))

print(f'''
        Rodada de Jokenpô
Você escolheu: {escolha_usuario}
O computador escolheu: {escolha_computador}
''')

if(escolha_computador == escolha_usuario):
    print('Deu empate!!')
elif(escolha_computador == 'pedra'):
    if(escolha_usuario == 'papel'):
        print('Você venceu!!')
    else:
        print('Você perdeu!!')
elif(escolha_computador == 'papel'):
    if(escolha_usuario == 'tesoura'):
        print('Você venceu!!')
    else:
        print('Você perdeu!!')
elif(escolha_computador == 'tesoura'):
    if(escolha_usuario == 'pedra'):
        print('Você venceu!!')
    else:
        print('Você perdeu!!')
        
