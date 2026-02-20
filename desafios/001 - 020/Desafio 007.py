# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('\nA média do alunos foi: {:.2f}'.format(media))