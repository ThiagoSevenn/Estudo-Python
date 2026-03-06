# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: Considere que os caixas possuem as cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

print('{:-^50}'.format('SAQUE BANCÁRIO'))

saque_imutavel = saque = int(input('Qual valor(inteiro) que deseja sacar? '))
cinquenta = vinte = dez = um = 0
while saque > 0:    
    if (saque // 50) > 0:
        cinquenta = saque // 50
        saque = saque % 50
    elif (saque // 20) > 0:
        vinte = saque // 20
        saque = saque % 20
    elif (saque // 10) > 0:
        dez = saque // 10
        saque = saque % 10
    elif (saque // 1) > 0:
        um = saque // 1
        saque = saque % 1
        
print('\n{: ^50}'.format('INFORMAÇÕES DO SAQUE'))
print(f'Cédulas de R$50,00: {cinquenta}')        
print(f'Cédulas de R$20,00: {vinte}')        
print(f'Cédulas de R$10,00: {dez}')        
print(f'Moedas de R$1,00: {um}')        
print(f'Preço total R${saque_imutavel:.2f}')        
print('{:-^50}'.format(''))