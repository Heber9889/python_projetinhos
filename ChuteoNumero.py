import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print("#----------------------------#\n| *Chute_Um_Valor_Mais_Baixo*|\n#----------------------------#\n :_")
                self.PedirValorAleatorio()

            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print("#--------------------------#\n|*Chute_Um_Valor_Mais_Alto*|\n#--------------------------#\n :_")
                self.PedirValorAleatorio()

            if int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print("#-----------------------#\n|-----------------------|\n|-----------------------|\n|-----------------------|\n|-----------------------|\n|*PARABENS*VOCE*ACERTOU*|\n|-----------------------|\n|-----------------------|\n|-----------------------|\n|-----------------------|\n|-----------------------|\n#-----------------------#\n :_")
          
    def PedirValorAleatorio(self):
        self.valor_do_chute = input("#-----------------------#\n|   Chute Um Numero:    |\n#-----------------------#\n :_")

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()