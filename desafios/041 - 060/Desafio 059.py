# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0
numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
while opcao != 5:
    opcao = int(input(
'''--------------------------------------------                  
        ESCOLHA A OPERAÇÃO DESEJADA:
[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Escolha: '''))
    print('--------------------------------------------')
    print(f'{f'OPERAÇÃO ESCOLHIDA {opcao}': ^30}\n')
    
    if opcao == 1:
        soma = numero_um + numero_dois
        print(f'A soma entre os dois números é de {soma}')
    if opcao == 2:
        multiplicar = numero_um * numero_dois
        print(f'A multiplicação entre os dois números é de {multiplicar}')
    if opcao == 3:
        maior = numero_um
        if numero_um < numero_dois:
            maior = numero_dois
        print(f'O maior entre os dois números é {maior}')
    if opcao == 4:
        numero_um = int(input('Digite um número: '))
        numero_dois = int(input('Digite outro número: '))
        
print('Fechando programa...')