# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: R$'))

print('''Opções:
1 ~> À vista dinheiro/cheque: 10% de desconto
2 ~> À vista no cartão: 5% de desconto
3 ~> Em até 2x no cartão: preço normal
4 ~> 3x ou mais no cartão: 20% de juros''')

opcao = int(input('Opção escolhida: '))

print()

if(opcao == 1):
    print(f'A compra à vista no dinheiro/cheque fica: R${(produto * 0.9):.2f}')
elif(opcao == 2):
    print(f'A compra à vista no cartão fica: R${(produto * 0.95):.2f}')
elif(opcao == 3):
    print(f'Em até 2x no cartão fica: R${produto:.2f}')
elif(opcao == 4):
    print(f'A compra 3x ou mais no cartão fica: R${(produto * 1.2):.2f}')
else:
    print('A opção escolhida não existe! Tente novamente.')