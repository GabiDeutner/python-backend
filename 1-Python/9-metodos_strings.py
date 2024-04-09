gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
                '''

print(gameName.upper()) #Maiúsculo
print(gameName.lower()) # Minúsculo
print(gameName.capitalize()) #Apenas primeira letra maiúscula
print(gameName.title()) #Apenas primeira letra maiúscula
print(gameName.center(10, '-')) #Retorna a string centralizada
print(gameName.find("f"))
print(gameDescription.count('a')) #Conta quantos caracteres 
print(gameDescription.count('A')) #Conta quantos caracteres 
print(gameDescription.replace("Fifa", "Pes")) #Altera elementos
print(gameDescription.split(','))