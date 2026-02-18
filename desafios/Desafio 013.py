# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite o salário do funcionário: '))

novo_salario = salario * 1.15

print('\nO salário do funcionário com aumento é de R${:.2f}'.format(novo_salario))