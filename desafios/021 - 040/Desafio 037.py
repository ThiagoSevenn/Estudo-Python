# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 ~> Para binário
# 2 ~> Para octal
# 3 ~> Para hexadecimal 

numero = int(input('Digite um número inteiro: '))

print('''
Escolha uma das opções de conversão:
1 ~> Para binário
2 ~> Para octal
3 ~> Para hexadecimal 
''', end='')
opcao = int(input('Escolha: '))

print()

if(opcao == 1):
    print(f'O número {numero} para binário é {bin(numero)}')
elif(opcao == 2):
    print(f'O número {numero} para octal é {oct(numero)}')
elif(opcao == 3):
    print(f'O número {numero} para hexadecimal é {hex(numero)}')
else:
    print('Não existe essa opção, tente novamente.')