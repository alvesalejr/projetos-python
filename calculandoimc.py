# Projeto de Aprendizado de Python - Calcular o IMC.

''' Lógica:
1: Preciso das informações do Usuário Altura / Peso e o Nome.
2: Preciso que ele digite as informações.
3: Preciso de um cálculo que me traga o resultado.
4: Preciso imprimir na tela o resultado pro usuário.

'''

def calcularimc():
    nome = input('Olá, digite o seu nome: ')
    altura = float(input(f'Olá, {nome} digite a sua altura: '))
    peso = float(input(f'{nome}, agora digite o seu peso: '))
    imc = peso / (altura * altura)

    if imc < 18.5:
        print(f'{nome}, você está abaixo do peso.')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'{nome}, você está no peso normal.')
    elif imc >= 25 and imc <= 29.9:
        print(f'{nome}, você está sobrepreso.')
    elif imc >= 30 and imc <= 34.9:
        print(f'{nome}, você está com obesidade Grau 1.')
    elif imc >= 35 and imc <= 39.9:
        print(f'{nome}, você está com obesidade Grau 2.')
    elif imc >= 40:
        print(f'{nome}, você está com obesidade Grau 3.')