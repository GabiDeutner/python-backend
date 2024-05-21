from decorators import my_decorator, uppercase_decorator, split_string

# Exemplo 1 - 
@my_decorator
def my_function():
    print("Dentro da função")

my_function()

# Exemplo 2 - Deixando uma string em maiúscula

@uppercase_decorator
def say_hi():
    return 'Olá mundo'

print(say_hi())

# Exemplo 3 - Múltiplos Decorators
@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())
