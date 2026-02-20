# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.  

numero_um = int(input('Digite o primeiro número: '))
numero_dois = int(input('Digite o segundo número: '))
numero_tres = int(input('Digite o terceiro número: '))

print()

if numero_dois >= numero_um:
    if numero_dois >= numero_tres:
        print(f'{numero_dois} é o maior.')
                
if numero_um >= numero_dois:
    if numero_um >= numero_tres:
        print(f'{numero_um} é o maior.')
        
if numero_tres >= numero_dois:
    if numero_tres >= numero_um:
        print(f'{numero_tres} é o maior.')

if numero_dois <= numero_um:
    if numero_dois <= numero_tres:
        print(f'{numero_dois} é o menor.')
                
if numero_um <= numero_dois:
    if numero_um <= numero_tres:
        print(f'{numero_um} é o menor.')
        
if numero_tres <= numero_dois:
    if numero_tres <= numero_um:
        print(f'{numero_tres} é o menor.')