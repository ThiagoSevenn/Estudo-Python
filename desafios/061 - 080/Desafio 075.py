# Crie um programa que tenha uma tupla única com nomes dos produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular
# Lápis -> 1.75
# Borracha -> 2
# Caderno -> 15.9
# Estojo -> 25
# Transferidor -> 4.2
# Compasso -> 9.99
# Mochila -> 120.32
# Caneta -> 22.3 
# Livro -> 34.9

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
tupla_produto_preco = (('Lápis',1.75),('Borracha',2),('Caderno',15.9),('Estojo', 25),('Transferidor',4.2),('Compasso', 9.99),('Mochila',120.32),('Canetas',22.3),('Livro',34.9))
for produto,preco in tupla_produto_preco:
    print(f'{produto:-<30}R${'{:.2f}'.format(preco):>8}')
print('-'*40)