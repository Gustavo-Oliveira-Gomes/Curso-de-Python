from math import hypot
cto = float(input('Qual e o cateto oposto : '))
cta = float(input('Qual e o cateto adjacente : '))

''' ctpo = cto ** 2
ctpa = cta ** 2
ctt = ctpa + ctpo
print('o comprimento da hipotenusa ... {:.2f}'.format(sqrt(ctt)))'''

print('O valor da hipotenusa sera de ... {:.2f}'.format(hypot(cto, cta)))
