gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.
                '''
line = '='
gameName = 'Fifa'
gameVersion = '24'
### Concatenando o nome do jogo ###
gameFullName = gameName + gameVersion

### Multiplicando a string ###
print(line*30)
print(gameFullName)
print(gameDescription)

### Buscando uma palavra na descrição ###
print("Fifa" in gameDescription)
print("futebol" in gameDescription)
print(line*30)