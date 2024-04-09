name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo\n"))
planIncluded = input("Está incluso no serviço mensal?\n")

print("###Dados do Jogo####")
print("====================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

# Alternativa 2
# print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
#       "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}")