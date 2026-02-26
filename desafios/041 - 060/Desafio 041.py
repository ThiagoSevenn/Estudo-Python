# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos : Infantil
# Até 19 anos : Junior
# Até 25 anos : Sênior
# Acima : Master
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))

idade = ano_atual - ano_nascimento

print(f'A idade do atleta é de {idade} anos')
if(idade <= 9):
    print('O atleta faz parte da categoria: Mirim.')    
elif(idade <= 14):
    print('O atleta faz parte da categoria: Infantil.')   
elif(idade <= 19): 
    print('O atleta faz parte da categoria: Junior.')  
elif(idade <= 25):  
    print('O atleta faz parte da categoria: Sênior.')
else:    
    print('O atleta faz parte da categoria: Master.')    
