tr1 = int(input('Primmeiro lado do triangulo:'))
tr2 = int(input('segundo lado do triangulo:'))
tr3 = int(input('treciero lado do triangulo:'))

if tr1 == tr2 and tr2 == tr3:
    print('triagulo Equilatero')
elif tr1 == tr2 or tr2 == tr3 or tr1 == tr3:
    print('triangulo Isoceles')
elif tr1 != tr2 and tr2 != tr3 and tr1 != tr3:
    print('triangulo escaleno')

print('fim do progama')
