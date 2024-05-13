gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]
"""
Em uma única expressão aplicamos o for e o 
if para selecionar jogos que tenham a letra a

Sintaxe: novalista = 
[expression for item in iterable if condition == True]

"""
newList = [x for x in gamesList if "a" in x]

print(newList)

gamesFinished = [x for x in gamesList if x != "Kirby"] 
print(gamesFinished)

listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)
