#reajuste de salario
slr = float(input('Qual e o seu salario?'))
if slr < 1250:
    sl = slr + (slr * 15 / 100)
else:
    sl = slr + (slr * 10 / 100)
print('O seu salario era de de {:.2f} e com o reajuste pasa a ser {:.2f}'.format(slr, sl))

