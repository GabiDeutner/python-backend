import math

# Acessar o número de Pi
print(math.pi)
# Formatando em duas casas decimais
print(f"{math.pi:.2f}")

# Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

# Arredondando números para cima e para baixo
num1 = 10.3
print(math.ceil(num1))
print(math.floor(num1))

# Fatorial de um número 
num2 = 7
print(math.factorial(num2))

# Potênciação de números
print(math.pow(5,5)) # equivale a 5 ** 5

# Raiz quadrada 
print(math.sqrt(169)) 

# Maior denominador comum - Reduzir frações
mdc = math.gcd(25, 120)
print(mdc)

# Logaritmo
print(math.log(10))
print(math.log(10, 3))
