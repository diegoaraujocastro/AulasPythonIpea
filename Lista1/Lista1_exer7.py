#Exercício 7

print('Temos uma lista e vou mostrar algumas informações interessantes dela. A lista é formada pelos valores -2, 34, 5, 10, 5, 4, 32. Agora valos lá:')

lista_exer7 = [-2, 34, 5, 10, 5, 4, 32]

print(f'Este é o primeiro valor: {lista_exer7[0]}')

print(f'Este é o último valor: {lista_exer7[-1]}')

soma = 0

a = len (lista_exer7)

for i in lista_exer7:
       soma = soma + i

print(f'A soma é {soma}')

print(f'A média é {soma/a:.2f}')

lista_ordem = sorted(lista_exer7)

mediana = lista_ordem[int(len(lista_ordem)/2)]

print(f'A médiana é {mediana:.2f}')