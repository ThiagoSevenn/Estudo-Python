# Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

print(f'{'PROGRAMA DE EXIBIR NÚMERO':-^50}\n')
contagem_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
                    'onze','doze','treze','quartoze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

numero = int(input('Digite um número que deseje saber o seu extenso(0 a 20):'))
print(f'\nO número {numero} se chama {contagem_extenso[numero]}')
print(f'{'END':-^50}')