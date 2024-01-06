nome = str(input('Qual e o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome femnino')
else:
    print('Seu nome e bem normal')
print('tenha um bom dia, {}'.format(nome))