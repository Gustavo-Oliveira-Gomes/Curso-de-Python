from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno:  '))
n3 = str(input('treceiro aluno: '))
n4 = str(input('Quarto aluno:   '))
liste = [n1, n2, n3, n4]
shuffle(liste)
print('A sequencia de alunos sera de')
print(liste)
