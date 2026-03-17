# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as sua vogais.

vogais = ('a','e','i','o','u')
palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','PROGRAMAÇAO','ESTUDO','TRABALHAR','MERCADO','PROGRAMADOR','PRATICAR')

for palavra in palavras:
    print('Na palavra "{}" temos '.format(palavra),end='')
    palavra = palavra.lower()
    for contador in range(len(palavra)):
        for vogal in vogais:
            if vogal == palavra[contador]:
                print('{} '.format(vogal),end='')
    print()