import random

class SimuladorDeDado:
    def __init__(self): #Função
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.nome = input('Olá, digite seu nome: ')
        self.mensagem = (f'Olá, {self.nome} você gostaria de gerar um valor? ')
        
    def Iniciar(self):
        resposta = input(self.mensagem)
        try: #Condição de SE ou NÃO.
            if self.eventos == 'Sim' or self.eventos == 'sim':
                self.GerarValorDoDado() #SE SIM, Chamando a Função gerarvalordado.
            elif self.eventos == 'Não' or self.eventos == 'não':
                print('Obrigado, volte sempre.')             
            else:
                print('Por favor, digite "Sim" ou "Não"')
                self.Iniciar() #SE NÃO, chamando a função de inicio.
        except:
                print('Ocorreu um erro')
                       
    def GerarValorDoDado(self): #Função para gerar o número.
        print("Valor gerado:", random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado() #Instanciando a Classe e a Função.
simulador.Iniciar()