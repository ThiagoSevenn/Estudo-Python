# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

aluno_um = input('Digite o nome do primeiro aluno: ')
aluno_dois = input('Digite o nome do segundo aluno: ')
aluno_tres = input('Digite o nome do terceiro aluno: ')
aluno_quatro = input('Digite o nome do quarto aluno: ')

print('\nO aluno escolhido foi: {}'.format(choice((aluno_um,aluno_dois,aluno_tres,aluno_quatro))))
