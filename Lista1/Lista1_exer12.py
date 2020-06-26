#Exercício 12

def eprimo (num):

    eprimo = True

    if num == 1:
        return False

    for i in range(2,num):
        if num%i == 0:
            eprimo = False

    if (eprimo == True):

        return True
    else:
        return False

aniversario = int(input("Qual o dia do teu aniversário?:"))

print("Confira a lista de números primos mais o dia do seu aniversário:")

for i in range(2,258):

    if(eprimo(i)):
     print(i)
print(aniversario)