class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"

movie = Movie("Super Mario", 2023, False, 10.0, 120)
print(movie)
print(f"Filme {movie.name} é de {movie.yearLaunch} e possui nota {movie.note}")
