n1 = int(input('digite o primeiro valor'))
n2 = int(input('digite o segundo valor '))
n3 = int(input('digite o terceiro valor'))
# verificando o menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verificando o maior valor

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('o maior  valor sera {}'.format(maior))
print('o menor  valor sera {}'.format(menor))
