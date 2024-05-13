'''
## Contagem Regressiva

Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
'''

#resolução 1 - sem o beep

x = 10
while x >= 0:
    print(x)
    x -= 1


# resolução 2 - com o beep
import winsound
x = 10
while x >= 0:
    print(x)
    x = x - 1
winsound.Beep(2500, 500) # frequencia, duração do beep


'''
## Tabuada

Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''

number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1
