class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro filme

movie = Movie()
movie.name = "Top Gun Maverick"
movie.yearLaunch = 2022
movie.includedPlan = False
movie.note = 5.0
print("####Dados Filme####")
print(f"Nome do Filme: {movie.name} - Ano de Lançamento: {movie.yearLaunch}")
