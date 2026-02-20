# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários acima de R$1250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário de um funcionário para calular o seu aumento: '))

if salario > 1250:
    salario = salario * 1.1
else :
    salario = salario * 1.15

print('O novo salário do funcionário é R${:.2f}'.format(salario))