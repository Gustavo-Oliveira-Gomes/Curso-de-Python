#triangulos
r1 = int(input('primeira reta:'))
r2 = int(input('segunda reta:'))
r3 = int(input('treceira reta:'))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Sim as retas forma um triangulo')
else:
    print('As retas nao formarao um triangulo')
