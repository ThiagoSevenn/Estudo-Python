# Refaça o "Desafio 035" dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero : Todos os lados iguais
# Isósceles : Dois lados iguais
# Escaleno : Todos os lados diferentes

reta_um = int(input('Digite a primeira aresta do triângulo: '))
reta_dois = int(input('Digite a segunda aresta do triângulo: '))
reta_tres = int(input('Digite a terceira aresta do triângulo: '))

print()

if(reta_um < (reta_dois + reta_tres)):
    if(reta_dois < (reta_um + reta_tres)):
        if(reta_tres < (reta_um + reta_dois)):
            print(f'Os lados {reta_um}, {reta_dois}, {reta_tres} formam um triângulo.')
            if(reta_um == reta_dois and reta_dois == reta_tres):
                print('O triângulo formado é um triângulo equilátero.')
            elif(reta_um != reta_dois and reta_um != reta_tres and reta_dois != reta_tres):
                print('O triângulo formado é um triângulo escaleno.')
            else:
                print('O triângulo formado é um triângulo isósceles.')
    
if(reta_um >= (reta_dois + reta_tres)):
    print('Esses lados não formam um triângulo.')            
if(reta_dois >= (reta_um + reta_tres)):
    print('Esses lados não formam um triângulo.')            
if(reta_tres >= (reta_um + reta_dois)):
    print('Esses lados não formam um triângulo.')   