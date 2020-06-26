#Exercício 9

def funcao (dic):

  for each in dic:

    if each in 'aeiou':
      dic[each] = dic[each] ** 2

    else:
      dic[each] = 0

  print (dic)

#Agora vamos testar a função com um dicionário qualquer:

print('Resultado final do loop:')

dic_teste = {'u': 10, 'z':2,'p':5,'i':4}

funcao (dic_teste)
