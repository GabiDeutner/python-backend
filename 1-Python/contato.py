'''
Exercício Final

Agenda de Contatos

Desenvolva uma agenda de contatos utilizando Programação Orientada a Objetos. O programa deve seguir as especificidades:

1. Ter uma classe Contact contendo os atributos: name, phone e email

2. Ter uma classe ContactBook contendo quatro métodos:
a.Um método para adicionar contato.
b.Um método para listar contatos.
c.Um método para buscar contatos.
d.Um método para remover contatos.

3. Criar um arquivo principal para a aplicação que deve instanciar as duas classes criadas anteriormente e 
desenvolver e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
'''

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
