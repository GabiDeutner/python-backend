class Movie:
    plataform = "OneBitFilmes"
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Plataforma: {Movie.plataform}")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.totalEvaluation}")
        print(f"Total Avaliadores: {self.evaluators}")
        print(f"Duração Filme: {self.durationMinutes}")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name} é: {self.totalEvaluation / self.evaluators}") 
    
        
movie = Movie("Super Mario", 2023, False, 120)
movie2 = Movie("Sonic", 2022, False, 110)
movie.evaluate(8.5)
movie.evaluate(9.0)
movie.technical_sheet()
movie.average()
# Modificando plataforma
Movie.plataform = "OneBitCode Pro"
movie2.evaluate(10.0)
movie2.evaluate(9.5)
movie2.technical_sheet()
movie2.average()
