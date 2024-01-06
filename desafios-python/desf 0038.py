n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2 and n2 < n1:
    print('O primeiro valor e maior {}'.format(n1))
elif n2 > n1 and n1 < n2:
    print('O sugendo valor e maior {}'.format(n2))
elif n1 == n2:
    print('Os dois valores sao iguas {} {}'.format(n1, n2))
print('Fim do Programa')
