#ano bissexto
from datetime import date
n = int(input('Digite o ano para saber se ele e bissexto? coloque 0 para analisar o ano atual:'))
if n == 0 :
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano {} e bissexto'.format(n))
else:
    print('O ano {} não e bissexto'.format(n))
