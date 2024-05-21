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

from contato import Contact
from contato_agenda import ContactBook

contact_book = ContactBook()

while True:
    print("\n--- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")

    choice = input("Escolha a opção: ")

    if choice == "1":
        name = input("Informe o nome: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o e-mail: ")
        contact = Contact(name, phone, email)
        contact_book.add_contact(contact)
        print("Contato adicionado com sucesso.")
    elif choice == "2":
        name = input("Informe o nome para remover: ")
        contact = contact_book.search_contact(name)
        if contact:
            contact_book.remove_contact(contact)
            print("Contato removido com sucesso.")
    elif choice == "3":
        contact_book.display_contacts()
    elif choice == "4":
        name = input("Procure por um nome: ")
        contact_book.search_contact(name)
    elif choice == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5")
