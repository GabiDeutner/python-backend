gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

for list in gamesList:
    print(list)

# 1 - Quando a condição for atendida, o loop será encerrado
for list in gamesList:
    if list == "God of War":
        break
    print(list)

# 2 - Quando a condição for atendida, o loop vai para a próxima iteração
for list in gamesList:
    if list == "God of War":
        continue
    print(list)

# 3 - Avaliação Jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo \n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating}")
