# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample

aluno_um = input('Digite o nome do primeiro aluno: ')
aluno_dois = input('Digite o nome do segundo aluno: ')
aluno_terceiro = input('Digite o nome do terceiro aluno: ')
aluno_quarto = input('Digite o nome do quarto aluno: ')

print(f'\nA ordem escolhida para essa apresentação foi {sample((aluno_um,aluno_dois,aluno_terceiro,aluno_quarto),k = 4)}')