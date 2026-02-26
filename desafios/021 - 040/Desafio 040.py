# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média antingida:
# Média abaixo de 5.0 : Reprovado 
# Média entre 5.0 e 6.9 : Recuperação
# Média 7.0 ou superior: Aprovado

nota_um = float(input('Digite a primeira nota do aluno: '))
nota_dois = float(input('Digite a segunda nota do aluno: '))

media = float(f'{((nota_um + nota_dois) / 2):.1f}')

print('\nA média foi:', media)
if(media < 5.0):
    print('O aluno está reprovado.')
elif(media >= 5.0 and media <= 6.9):
    print('O aluno está recuperação.')
else:
    print('O aluno está aprovado!!!')