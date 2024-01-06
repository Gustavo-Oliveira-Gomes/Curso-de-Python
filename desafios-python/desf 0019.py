from random import choice
nm1 = str(input('Qual e o primeiro nome: '))
nm2 = str(input('Qual e o segundo nome:  '))
nm3 = str(input('Qual e o treceiro nome: '))
nm4 = str(input('Qual e o quarto nome:  '))
lista = [nm1, nm2, nm3, nm4]
print('O aluno escolido foi {}'.format((choice(lista))))
