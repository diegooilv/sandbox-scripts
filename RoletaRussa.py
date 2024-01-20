from random import choice 
from random import randint
from random import seed as sd

def vef(valor):
    while True:
        if valor < 1 or valor > 6:
            try:
                valor = int(input("Escolha valores aceitáveis! "))
            except ValueError:
                print("Digite um valor numérico na próxima!!")
        else:
            return True
            
def roletaRussa():
    com_bala = []
    com_balan = 1
    for i in range(5):
        possibilidades = [1, 2, 3, 4, 5, 6]
        com_bala = []
        for ii in range(com_balan):
            seed = randint(1, 500)
            sd(seed)
            escolha = choice(possibilidades)
            com_bala.append(escolha)
            possibilidades.remove(escolha)
        try:
            escolha = int(input("Faça sua escolha: "))
        except ValueError:
            print("Escolha algum valor numérico na próxima!!")
            return
        if vef(escolha):
            if escolha in com_bala:
                print("Morreu!")
                return
            else:
                com_balan += 1
    print("Você venceu!!!")

roletaRussa()
