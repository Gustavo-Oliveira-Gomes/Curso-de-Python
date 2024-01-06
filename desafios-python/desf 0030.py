vl = int(input('Digite um valor para saber se e impar ou par'))
v = vl % 2
if v == 0:
    print('O numero {} e Par'.format(vl))
else:
    print('O numero {} e Impar'.format(vl))