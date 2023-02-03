''' 

Lógica: Projeto de Aprendizado de Python - Calcular o IMC.
1: Preciso das informações do Usuário Altura / Peso e o Nome.
2: Preciso que ele digite as informações.
3: Preciso de um cálculo que me traga o resultado.
4: Preciso imprimir na tela o resultado pro usuário.

'''

class CalcularImc:
    def __init__(self):
        self.nome = input('Olá, digite o seu nome: ')
        self.altura = float(input(f'Olá, {self.nome} digite a sua altura: '))
        self.peso = float(input(f'{self.nome}, agora digite o seu peso: '))
        self.imc = self.peso / (self.altura * self.altura)

    def Calcular(self): #Função pra calcular
        
        if self.imc < 18.5:
            print(f'{self.nome}, você está abaixo do peso.')
        elif self.imc >= 18.5 and self.imc <= 24.9:
            print(f'{self.nome}, você está no peso normal.')
        elif self.imc >= 25 and self.imc <= 29.9:
            print(f'{self.nome}, você está sobrepreso.')
        elif self.imc >= 30 and self.imc <= 34.9:
            print(f'{self.nome}, você está com obesidade Grau 1.')
        elif self.imc >= 35 and self.imc <= 39.9:
            print(f'{self.nome}, você está com obesidade Grau 2.')
        elif self.imc >= 40:
            print(f'{self.nome}, você está com obesidade Grau 3.')

calculador = CalcularImc()
calculador.Calcular()