''' 
Lógica: Projeto de Aprendizado de Python - Simular um Dado
'''
import random

class SimuladorDeDado:
    def __init__(self): # Função
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Olá, você gostaria de gerar um novo valor? '
        
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'Sim' or resposta == 'sim':
                self.GerarValorDoDado()
                
            elif resposta == 'Não' or resposta == 'não':
                print('Obrigado, volte sempre.')
                
            else:
                print('Por favor, digite "Sim" ou "Não"')
                return input(self.mensagem)
        except:
            print('Ocorreu um erro')
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()