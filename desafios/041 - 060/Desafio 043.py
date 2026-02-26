# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 : Abaixo do peso
# Entre 18.5 e 25 : Peso ideal
# 25 até 30 : Sobrepeso
# 30 até 40 : Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

imc = round((peso / (altura ** 2)),1)

print(f'\nO IMC dessa pessoa é {imc}.')
if(imc < 18.5):
    print('A pessoa está abaixo do peso ideal.')
elif(imc < 25):
    print('A pessoa está no peso ideal.')
elif(imc < 30):
    print('A pessoa está no sobrepeso.')
elif(imc < 40):
    print('A pessoa está na obesidade.')
else:   
    print('A pessoa está na obesidade mórbida.')