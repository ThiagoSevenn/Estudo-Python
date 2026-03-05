# Melhore o "Desafio 061", perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos

primeiro_termo = float(input('Primeiro termo de uma PA: '))
razao = float(input('Qual a razão dessa PA: '))
dez_primeiros_termos = 1
print('{:-^40}'.format('OS 10 PRIMEIROS TERMOS'))
mais_termos = termos = 10
while mais_termos != 0:
    while dez_primeiros_termos != (termos + + 1):
        termo_n = primeiro_termo + (dez_primeiros_termos - 1) * razao
        print(f'O {dez_primeiros_termos}º termo: {termo_n}')
        dez_primeiros_termos += 1
    print('{:-^40}'.format('-'))    
    mais_termos = int(input('Deseja saber mais quantos termos? '))
    termos += mais_termos
print('{:-^40}'.format('FIM'))