nome = str(input('Qual e o seu nome')).strip()
nomelist = nome.split()
print('Primeiro nome = {}'.format(nomelist[0]))
print('O ultimo nome = {}'.format(nomelist[len(nomelist)-1]))
