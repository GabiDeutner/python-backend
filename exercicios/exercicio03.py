'''
## Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
'''

dist = int(input("Qual a distância que você deseja percorrer? - km")
preco

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.35

print(f"o valor da viagem é: R$ {preco: .2f}")



'''
## Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.

'''

sal = float(input("Qual o seu salário?"))
perc_increase = 0.15
if sal > 1250:
    perc_increase = 0.10
increase = sal * perc_increase
print(f"Seu aumento será de: R$ {increase:.2f}")

