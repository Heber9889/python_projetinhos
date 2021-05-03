import random 

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "#-----------------------------------------------#\n|        Voçê Gostaria De Jogar o Dado?         |\n#-----------------------------------------------#\n     :"

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:        
            if resposta == "sim" or "yes" or "ok" or resposta == "s" or "y" :
                self.GerarValorDoDado()
            elif resposta == "nao" or "exit" or "quit" or  resposta == "n" :
                print("#-----------------------------------------------#\n|            (: Obrigado Por Jogar :)           |\n#-----------------------------------------------#")
            else:
                print("#---------------------------------------------------------#\n| Ocoreu Um Erro Responda Com (sim) ou (nao) Obrigado!    |\n#---------------------------------------------------------#")
        except:
            print("Ocoreu Um Erro Ao Reseber A Sua Mensagem")
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = SimuladorDeDado()
simulador.Iniciar()

                      
            
        
