### Presente a partir do 'Desafio 022' - 'Desafio 027 ###

# Cadeia de caracteres ou String é armazenada na memória como um conjunto de caracteres individuas,
# o espaço(' ') também conta como caracter.

#### Fatiamento de uma string ####
frase = 'Essa é uma string de exemplo.'

print(f'A frase exemplo: "{frase}"\n')

## Pegar uma letra
print('Uma só letra (posição 9): '+frase[9])

print()
## Pegar um trecho da frase
print('Um trecho da frase (trecho da posição inicial até a posição 15, excluindo a 15): '+frase[:15])
print('Um trecho da frase (trecho da posição 7 até o final da frase): '+frase[7:])
print('Um trecho da frase (trecho da posição 7-15, excluindo o 15): '+frase[7:15])

print()
## Pegar um trecho da frase, pulando de x em x caracteres. No exemplo usarei 2 em 2.
print('Pegar um trecho da frase (trecho da posição inicial até a posição 15, excluindo a 15), pulando de 2 em 2 caracteres: '+frase[:15:2])
print('Pegar um trecho da frase (trecho da posição 7 até o final da frase), pulando de 2 em 2 caracteres: '+frase[7::2])
print('Pegar um trecho da frase (trecho da posição 7-15, excluindo o 15), pulando de 2 em 2 caracteres: '+frase[7:15:2])
print('Pegar a frase inteira, pulando de 2 em 2 caracteres: '+frase[::2])

print()

#### Análise de uma string ####

## Tamanho de uma string
print('Tamanho da frase exemplo: {}'.format(len(frase)))

print()
## Contar quantos caracteres 'x' aparecem na frase. Como exemplo usarei 'o'
print('Contar quantos caracteres "o" aparecem na string: ',frase.count('o'))
print('Contar quantos caracteres "o" aparecem na string do fatiamento [0:10]: ',frase.count('o',0,10))

print()
## Localiza tal string em uma string maior, se ela tiver na string, a função devolve
## o número da primeira aparição caso contrário devolverá -1. Por exemplo "a "
print('Localiza número da primeira aparição de tal string em uma string maior: ',frase.find('a '))
print('Caso contrário devolverá -1: ',frase.find('oba'))

print()
## Verificar se existe tal string em outra string
print('A string "exemplo" está na string? {}'.format('exemplo' in frase))

print()

#### Transformação ####

## Substituir tal string por outra
print(frase.replace('exemplo', 'prática'))

print()
## Deixar todas os caracteres maiúsculos(upper) e minúsculos(lower)
print(frase.upper())
print(frase.lower())

print()
## Deixar apenas o primeiro caracter da string em maiúsculo
frase_nova = frase.upper()
print(frase_nova.capitalize())

## Deixar todo caracter que vier depois de espaço em maiúsculo.
print(frase_nova.title())

print()
## Tirar os espaços antes e depois de começar a frase.
frase_nova = '  Aprendendo Python  '

print(frase_nova.strip())

## Algumas funções tem essa disponibilidade de fazer pela direita e esquerda, tem que testar (não são todas)
## Tirar os espaços a esquerda(lstrip) e os da direita(rstrip)
print(frase_nova.rstrip())
print(frase_nova.lstrip())

print()
#### Divisão ####

## Dividir a string a partir de uma string menor. Como por exemplo, vou pegar a variável frase_nova e dividir ela por ' '
print(frase_nova.split(' '))

print()
#### Junção ####

## Juntar todos os elementos de uma determinada frase utilizando um caracter ou string de sua escolha. 
## Por exemplo, utilizarei '-' para juntar o que foi separado anteriormente
print('-'.join(frase_nova.split(' ')))
