# Refaça o "Desafio 051", lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrututra while

primeiro_termo = float(input('Primeiro termo de uma PA: '))
razao = float(input('Qual a razão dessa PA: '))
dez_primeiros_termos = 1
print('{:-^40}'.format('OS 10 PRIMEIROS TERMOS'))
while dez_primeiros_termos != 11:
    termo_n = primeiro_termo + (dez_primeiros_termos - 1) * razao
    print(f'O {dez_primeiros_termos}º termo: {termo_n}')
    dez_primeiros_termos += 1
    
print('{:-^40}'.format('FIM'))