#Exercício 5:

def recebe_letra():
    if x in ("a", "e", "i", "o", "u"):
        print('vogal')
    else:
        print ('consoante')

if __name__ == '__main__':
    x = input('Entre com uma letra. Vamos identificar para você se é consoante ou vogal:')
    recebe_letra()
