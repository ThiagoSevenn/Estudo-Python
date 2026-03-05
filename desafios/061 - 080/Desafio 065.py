# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menos valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
repeticao = int(input('Quantos números deseja digitar? '))
maior = menor = numero = int(input('Digite um número inteiro: '))
quantidade_numeros = 1
while repeticao != 0:
    if quantidade_numeros == 1:
        repeticao -= 2
    else:
        repeticao -= 1
        
    soma += numero
    quantidade_numeros += 1
    numero = int(input('Digite um número inteiro: '))
    if numero > maior:
        maior = numero
            
    if numero < menor:
        menor = numero

    if repeticao == 0:
        media = soma / quantidade_numeros
        print(f'{'INFORMAÇÕES':-^30}')
        print(
        f'''
Total de números digitados: {quantidade_numeros}
Média total: {media}
Maior número: {maior}
Menor número: {menor}
        ''')
        print(f'{'':-^30}')
        repeticao = int(input('Deseja digitar mais números(Se sim, digite a quantidade. Se não, digite 0)? '))
        