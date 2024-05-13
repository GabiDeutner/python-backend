def wellcome():
    print("Hello World")

def create_game():
    name = input("Digite o nome do jogo \n")
    yearLaunch = int(input("Digite o ano de lançamento\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

wellcome()
create_game()
