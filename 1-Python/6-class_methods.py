"""
1 - O método de classe utliza o primeiro parâmetro cls referente a classe
2 - O método de classe pode acessar ou modificar o estado da classe 
3 - Usamos o decorator @classmethod em python para criar um método de classe
""" 
class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))

wiiU = Console.from_text("Meu video game é WiiU e o preço é 1000")
ps5 = Console.from_text("Meu video game é Ps5 e o preço é 5000")
xboxOne = Console.from_text("Meu video game é XboxOne e o preço é 4600")
print(wiiU.__dict__)
print(ps5.__dict__)
print(xboxOne.__dict__)
