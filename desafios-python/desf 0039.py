from datetime import date
anon = int(input('Ano de nacimento: '))
n = date.today().year
d = anon - n
if d < 18:
    t = 18 - d
    print('Você ainda vai se alistar ')
    print('Ainda falta {} '.format(t))
elif d == 18:
    print('Hora de se alista')
elif d > 18:
    t = 18 - d
    print('O seu tempo de se alsitar ja passou ')
    print('Ja se passou do seu tempo de alistamento {} '.format(t))
