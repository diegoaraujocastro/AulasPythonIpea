#Exercício 2

def print_star():
    q = int(input('Informe a quantidade máxima de estrelas que você deseja que eu imprima na linha central: '))
    for i in range((q - 1) + 1):
        print('* ' * i)
    for i in range((q - 1), -1, -1):
        print('* ' * (i + 1))

if __name__ == '__main__':
    print_star()