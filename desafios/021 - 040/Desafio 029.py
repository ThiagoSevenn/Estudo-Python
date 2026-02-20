# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade de um carro: '))

print(f'Sua velocidade: {velocidade}km/h')
if velocidade > 80:
    print('Você foi multado por exesso de velocidade. Terá que pagar a multa de R${:.2f}'.format((velocidade - 80) * 7.0))
else :
    print('Você se livrou da multa!!')