# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços
frase_original = input('Digite uma frase que deseja verificar se é palíndromo:\n~~> ')

frase = frase_original.replace(" ",'').lower()
string = ''

for i in range(len(frase) - 1, -1,-1):
    string += frase[i]
 
palindromo = True if frase == string else False
 
print('A frase "{}" é um palíndromo'.format(frase_original) if palindromo else 'A frase "{}" não é um palíndromo'.format(frase_original))
