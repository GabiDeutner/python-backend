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

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Lista de Contatos vazia.")
        else:
            for contact in self.contacts:
                print(contact)
                print("----------------------")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print("Contato não encontrado.")
