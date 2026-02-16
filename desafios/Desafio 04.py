# Faça um programa que receba um input e mostre na tela o seu time primitivo e todas as possíveis informações sobre ela. 
# Utilize as funções '.is...'

input = input('Digite algo: ')

print('O input pertence a classe:', input.__class__)
print('O input é exclusivamente do alfabeto:',input.isalpha())
print('O input é exclusivamente numérico:',input.isnumeric())
print('O input é exclusivamente do alfabeto ou numérico:',input.isalnum())
print('O input é exclusivamente um espaço:',input.isspace())
print('O input é exclusivamente minúsculo:',input.islower())
print('O input é exclusivamente maiúsculo:',input.isupper())
print('O input tem a primeira letra maiúscula:',input.istitle())
