# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

print('{:-^40}'.format('CADASTRO DE PESSOAS'))

homens = mulheres_menos_vinte = maioridade = 0
while True:
    idade = int(input('Qual a idade da pessoa que deseja cadastrar? '))
    sexo = input('Qual o sexo da pessoa que deseja cadastrar?(feminino/masculino) ').lower()
    
    if idade > 18:
        maioridade += 1
    if sexo == 'masculino':
        homens += 1
    if sexo == 'feminino' and idade < 20:
        mulheres_menos_vinte += 1
        
    continuar = input('\nDeseja realizar o cadastro de mais uma pessoa?(s/n) ').lower()
    print()
    if continuar == 'n':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print('Quantidade de pessoas com mais de 18: {} pessoas\nForam cadastrados {} homen(s)\nUm total de {} mulher(es) tem menos de 20 anos'.format(maioridade,homens,mulheres_menos_vinte))