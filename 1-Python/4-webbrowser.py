import webbrowser

feito = False

while not feito:
    print("O que você deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre Módulos")
    print("3. Aprender Python, FullStack JS, Inglês e No Code")
    print("4. Sair")

    escolha = input("> ")

    if escolha == "1":
        webbrowser.open("http://www.python.org")
    elif escolha == "2":
        webbrowser.open("https://docs.python.org/3/py-modindex.html")
    elif escolha == "3":
        webbrowser.open("https://pages.onebitcode.com/")
    elif escolha == "4":
        feito = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 a 4")
