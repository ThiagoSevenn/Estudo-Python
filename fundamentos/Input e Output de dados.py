# Inputs
nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
# Input - Tipado
idade_tipado = int(input('Qual é a sua idade?'))

print('________________________________________') 

# Outputs
print('Olá ' + nome + ', então você possui' ,idade, 'anos.\n') 
# Output dos tipos
print('Tipagem primeira idade:',idade.__class__)
print('Tipagem segunda idade:',idade_tipado.__class__)