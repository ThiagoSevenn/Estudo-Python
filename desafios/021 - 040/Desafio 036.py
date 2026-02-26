# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.    

valor_casa =  float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo_pagamento = int(input('Quantos anos ele vai pagar? '))

prestacao = (valor_casa / (tempo_pagamento * 12))

print('\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa,tempo_pagamento,prestacao))
if(prestacao > (salario * 0.3)):
    print('Empréstimo negado.')
else:
    print('O empréstimo foi aceito.')