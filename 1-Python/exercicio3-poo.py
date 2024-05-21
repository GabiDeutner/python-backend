'''
Exercício 3

Cadastro de Viagem

Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:

1- Usuário deve informar o seu nome para cadastrar uma viagem.
2- Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.
3- Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no destino específico foi feito com sucesso.

'''


class Trip:
    def __init__(self, destiny):
        self.destiny = destiny

from exercicio3 import Trip

trip_0 = Trip("Lençóis Maranhenses")
trip_1 = Trip("Florianópolis")
trip_2 = Trip("Gramado")
trip_3 = Trip("Campos do Jordão")
trip_4 = Trip("Caldas Novas")

print("E aí viajante. Temos algumas ofertas para você!")
traveler = input("Digite seu nome para começarmos: ")
print(f"{traveler} temos 5 destinos que combinam com você:"
'''
[0] Lençóis Maranhenses
[1] Florianópolis
[2] Gramado
[3] Campos do Jordão
[4] Caldas Novas''')

choice = int(input("Selecione o destino da viagem desejada: "))   
list_trip = [trip_0, trip_1, trip_2, trip_3, trip_4]     

for option in list_trip:
    if choice >= 5:    #caso usuário não digite a opção correta
        print("Esta opção não está incluída em nossos destinos.")
        break
    if choice <= 4:     #verifica a seleção
        print(f"{traveler} sua viagem para {list_trip[choice].destiny} está marcada.") #resultado
        print("Volte sempre!")
        break
