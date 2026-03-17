# Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol', 'na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados da tabela
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição está o time do Mirassol

times = ("Palmeiras", "São Paulo", "Bahia", "Flamengo", "Coritiba", "Fluminense", "Athletico-PR", "Corinthians", "Red Bull Bragantino", "Grêmio", "Mirassol",
         "Chapecoense", "Atlético-MG", "Santos", "Vitória", "Botafogo", "Remo", "Internacional", "Cruzeiro", "Vasco")
print(f'{'TABELA DO BRASILEIRÃO - SÉRIE A':-^50}\n')
print(f'Primeiros 5 colocados da tabela: {times[:5]}')
print(f'Últimos 4 colocados da tabela: {times[-4:]}')
print(f'Lista com os times ordenados alfabeticamente: \n{sorted(times)[:10]}\n{sorted(times)[10:]}')
print(f'Posição do time do Mirassol: {times.index('Mirassol')}')
print(f'{'END':-^50}')