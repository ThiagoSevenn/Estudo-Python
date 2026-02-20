### Presente a partir do 'Desafio 016' ###

# Assim como outras linguagens de programação o python é cheio de bibliotecas 
# que disponibilizam ao programa utilizar diversos recursos diferentes visando suprir as necessidades do programador.

# Esses módulos podem ser desenvolvidos pelo próprio programador ou por terceiros, ambas necessitam da importação para ser utilizada.
# Porém, caso precise de uma biblioteca externa, comumente será necessário instalar ela.


## Em python existem duas formas diferentes de se importar uma biblioteca:
## 1ª ~> Utilizando "Importe *Nome da biblioteca*", esse import é mais generalizado
## 2ª ~> Utilizando "From *Nome da biblioteca* import *Nome da funcionalidade*", esse import é mais objetivo

# Por exemplo:

## 1ª forma:
# import math

# print(f'Esse é o 5! ~> {math.factorial(5)}')

## 2ª forma: Essa forma é otimizada devido a requisição ser mais específica,
#            sem guardar na memória funções que não serão utilizadas.
from math import factorial

print(f'Esse é o 5! ~> {factorial(5)}')
