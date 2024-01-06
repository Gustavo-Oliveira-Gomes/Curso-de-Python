from random import randint
n1 = int((input(randint(0, 5))))
print('estou a pensar em numero entra 0 e 5 consegui adivinhar qual seria esse numero ??')
n2 = int((input('Qual foi o numero que o computador escolheu ')))
if n2 == n1:
    print('O você acertou o numero escolhido')
else:
    print('Você erro o numero que pensei tente denovo')
print('O numero escolhido por mim foi{}'.format(n1))
