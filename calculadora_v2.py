saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

while saida.lower() != 'n':
    try:
        valor1 = float(input('Digite o primeiro número: '))
        valor2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação desejada (+, -, *, / ou o nome da operação): ')

        resultado = calculadora(valor1, valor2, operacao)

        print(f'Resultado da operação: {resultado}')

        saida = input('Deseja continuar? (S/N): ')
    except ValueError:
        print('Entrada inválida. Por favor, insira números válidos')