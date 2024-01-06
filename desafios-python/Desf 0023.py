nr = input('Digite um numero: ')
u = nr // 1 % 10
d = nr // 10 % 10
c = nr // 100 % 10
m = nr // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
