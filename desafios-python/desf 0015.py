km = float(input('Quantos kilometros forao percoridos : '))
dy = int(input('Quantos dias ficou com o carro: '))
kms = km * 0.15
dys = dy * 60
tot = kms + dys
print('O valor por km {}'.format(kms))
print('O valor por dia {}'.format(dys))
print('O valor Total {:.2f}'.format(tot))