#Exercício 8

#Dado o dicionário:
d = {'a':0}

#Acrescentando um par chave valor pedido:
d['b'] = '1'

#imprimindo d para verificar se foi inserido com sucesso:
print('O resultado é:')

print(d)

#verificando se "c" está presente.
print('c' in d.keys())

#Criando outro dicionário
e = {'z': 23}

#Concatenando
d.update(e)

#Resultado final

print(d)
