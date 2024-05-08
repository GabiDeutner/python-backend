import pprint 
gamesDict = {
  "fifa 23" : {
    "yearLaunch" : 2022,
    "classification" : 8.5,
    "genre": ["esporte", "família"]
  },
  "mario odyssey" : {
    "yearLaunch" : 2017,
    "classification" : 10.0,
    "genre": ["aventura", "3d"]
  },
  "donkey kong country" : {
    "yearLaunch" : 1996,
    "classification" : 9.5,
    "genre": ["aventura", "plataforma"]
  }
}

#print
pp = pprint.PrettyPrinter(depth=4)

#print(dictJogos)
pp.pprint(gamesDict)

# 1 - Buscando informação dentro de um dicionário
pp.pprint(gamesDict['fifa 23']['genre'])

# 2 - Adicionando novo item
gamesDict['fifa 23']['players'] = 1
pp.pprint(gamesDict['fifa 23'])

# 3 - Excluindo um dicionário
del gamesDict["fifa 23"]
pp.pprint(gamesDict)