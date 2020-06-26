#Exercício 11

#Definindo a função:
def funcao (list_teste):
# Organizando para a contagem
  list_teste.sort()
#Criando o dicionário, organizando em keys e calculando a frequência:
  dicionariot = dict()
  for each in list_teste:
    dicionariot[each] = dicionariot.get(each, 0) + 1
  print (dicionariot)

#Testando:

list_teste =  [0,4,30,8,10,15]

print(f'Ao testar a organização de keys e frequência, temos que, para a lista {list_teste}, chegamos aos seguintes quantitativos:')

funcao (list_teste)
