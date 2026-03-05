### Presente a partir do 'Desafio 028' ###

# Representam possibilidades, ou seja, mais de uma opção para algo ocorrer. Para expressar essa situação de condição utiliza-se a seguinte sintaxe:
# 'Se *algo acontecer(condição)* faça tal coisa, Senão algo acontece'
# Como as linguagens de programação, normalmente, são em inglês a sintaxe correta é: 'if ... else ...'
# Mas não se prenda a isso, pois o 'if' pode aparecer sozinho, como também pode aparecer aninhado(um if dentro de outro if) e também pode ser usado a seguinte sintaxe
# 'if ... elif ... else ...', Isso ocorre quando você precisa de duas ou mais condições que 'Disputam'. Será mais fácil entender com exemplos...

if(2 == 2):
    print('Claro que 2 é igual a 2.\n')
    
if(int(input('Digite um número: ')) == 2):
    print('Ta com imperfoco no 2?! Só pode')
else:
    print('Amém que você não digitou 2.')
   
print()
# Apenas pra mostrar que ocorre a verificação mesmo que nada aconteça 
if(3 == 2):
    print('Claro que 2 é igual a 2.\n')

nome = input('Digite seu primeiro nome: ')

print()

## Exemplo com elif (Condicional aninhada)
if(nome == 'joaozin'):
    print('Opa, como vai joaozin?')
elif(nome == 'jotinha'):
    print('Opa, como vai jotinha?')
else:
    print('Eu definitivamente não te conheço.')
    
## Uma outra forma de escrever essa condicional que é mais compacta e intuitiva é chamada de 'short-if-else'
print('Eae rapaz que não conheço' if ((nome != 'joaozin') and (nome != 'jotinha')) else 'Opa, eu te conheço!!') ## Utilizei "and" que ainda será apresentado.

## No python não existe operador ternário!!!