# Exercício 13

numero_original = input('informe um número acima de 999,00 no padrão brasileiro de formatação e com duas casas após a vírgula:')

print(numero_original)

numero_convertido = numero_original.translate({ord(','): '.', ord('.'): ','})

print(f'O valor reformatado para textos em inglês, ou seja, o ponto como separador decimal e a vírgula como agrupador de milhar é: {numero_convertido}')
