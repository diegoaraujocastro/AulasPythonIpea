#Exercício 3:

def funcao():
  a = 3
  b = 5
  for n in range(23,84):
    if n % a == 0 and n % b == 0:
        print ("Pumbla")
    elif n % a == 0:
        print ("Pum")
    elif n % b == 0:
        print ("Bla")
    else:
        print (n)

if __name__ == '__main__':
    print ("Abaixo temos uma lista com os números de 23 a 83. Todavia, quando for múltiplo de três será impresso Pum; quando for múltiplo de cinco será Bla, e quando for de ambos será PumBla:")
    funcao()








