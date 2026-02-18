# Escreva um programa que converta uma temperatura digitada em °C para °F.
temperatura_celsius = float(input('Digite a temperatura em graus Celsius que deseja converter: '))

temperatura_fahrenheit = ((temperatura_celsius * 9) / 5) + 32

print(f'A temperatura de {temperatura_celsius:.1f} °C significa {temperatura_fahrenheit:.1f} °F.')