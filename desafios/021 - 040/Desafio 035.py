# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_um = int(input('Digite a primeira aresta do triângulo: '))
reta_dois = int(input('Digite a segunda aresta do triângulo: '))
reta_tres = int(input('Digite a terceira aresta do triângulo: '))

print()

#### Forma mais simples de chegar ao resultado pedido.
if(reta_um < (reta_dois + reta_tres)):
    if(reta_dois < (reta_um + reta_tres)):
        if(reta_tres < (reta_um + reta_dois)):
            print(f'Os lados {reta_um}, {reta_dois}, {reta_tres} formam um triângulo.')
    
if(reta_um >= (reta_dois + reta_tres)):
    print('Esses lados não formam um triângulo.')            
if(reta_dois >= (reta_um + reta_tres)):
    print('Esses lados não formam um triângulo.')            
if(reta_tres >= (reta_um + reta_dois)):
    print('Esses lados não formam um triângulo.')            

## Achando o maior lado e verificando se forma ou não um triângulo, utilizando condicional aninhada
'''
if reta_um >= reta_dois:
    if reta_um >= reta_tres:
        if(reta_tres + reta_dois) > reta_um:
            print(f'Os lados {reta_um}, {reta_dois}, {reta_tres} formam um triângulo.')
        else:
            print('Esses lados não formam um triângulo.')            
elif reta_dois >= reta_um:
    if reta_dois >= reta_tres:
        if(reta_tres + reta_um) > reta_dois:
            print(f'Os lados {reta_um}, {reta_dois}, {reta_tres} formam um triângulo.')
        else:
            print('Esses lados não formam um triângulo.')
elif reta_tres >= reta_dois:
    if reta_tres >= reta_um:
        if(reta_um + reta_dois) > reta_tres:
            print(f'Os lados {reta_um}, {reta_dois}, {reta_tres} formam um triângulo.')
        else:
            print('Esses lados não formam um triângulo.')
'''