# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

primeiro_termo = float(input('Digite o primeiro termo de um PA: '))
razao = float(input('Digite a razão de uma PA: '))
print('Os 10 primeiros termos da PA:')
for numero in range(1,11):
    termo_geral = primeiro_termo + ((numero - 1)*razao)
    print('Termo {}º: {}'.format(numero,termo_geral))