import hashlib 
# Todos os algoritmos disponíveis
print(hashlib.algorithms_available)
# Algoritmos disponível de acordo com o SO
print(hashlib.algorithms_guaranteed)

algorithm = hashlib.sha256()
# Hash que é usado para criptografia do algoritmo
print(algorithm.digest())

# Criptografia de textos com Sha256
sha = hashlib.sha256()
message = "A melhor forma de prever o futuro é criá-lo".encode()
sha.update(message)
print(sha.hexdigest())

# Criptografia de textos com MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
