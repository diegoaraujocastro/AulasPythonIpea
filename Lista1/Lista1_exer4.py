# Exercício 4
def numeros():
    a = 13
    b = 19
    c = int(input('Qual o ano de nascimento da sua mãe?:'))
    for ano in range(c, 2728):
        if ano % a == 0 or ano % b == 0:
            print(ano)

if __name__ == '__main__':
    print('Agora vamos imprimir os números divisíveis por 13 e por 19 a partir do ano de nascimento da sua mãe até 2728:')
    numeros()