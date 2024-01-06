from datetime import date
ano = int(input('Qual e a sua idade?'))
n = date.today().year
d = n - ano
print(d)
if d <= 9:
    print('Mirim')
elif d <= 14:
    print('Infantil')
elif d <= 19:
    print('junior')
elif d == 20:
    print('Seniõr')
elif d >= 21:
    print('Mâster')
print('Essa sera sua classe de atuação')
