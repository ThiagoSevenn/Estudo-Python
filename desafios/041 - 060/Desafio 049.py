# Refaça o "Desafio 009", mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for

tabuada = int(input('Digite um número inteiro que deseje ver sua tabuada: '))
print('A tabuada do número {}, será:'.format(tabuada))
for numero in range(1,11):
    print(f'{tabuada} x {numero} = {tabuada * numero}')
