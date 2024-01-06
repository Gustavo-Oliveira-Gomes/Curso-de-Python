n = int(input('Qual e o valor? '))
print('1 para binaro')
print('2 para octal')
print('3 para hexadecimal')
nr = int(input('Em qual vc dejesa tranformar? '))
if nr == 1:
    nm = n
    print('o valor {} em binario ficara {}'.format(n, bin(nm)[2:]))
elif nr == 2:
    nm = n
    print('O valor {} em octal ficara {}'.format(n, oct(nm)[2:]))
elif nr == 3:
    nm = n
    print('O valor {} em hexadecimal ficara {}'.format(n, hex(nm)[2:]))

else:
    print('ERRO')

print('fim do programa')