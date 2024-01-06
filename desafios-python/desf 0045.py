from random import choice
print('----------------------------------')
print('JOGO JOKENPO PEDRA PAPEL E TESOURA')
print('----------------------------------')
pcjk = str(input(choice(['PEDRA', 'PAPEL', 'TESOURA'])))
print(pcjk)
jokepo = str(input('Qual vc ira jogar? ')).upper()

if 'pcjk' == 'jokepo':
    print('Empate leu a mente da maquina em')

elif pcjk == 'PEDRA':
    print('A maquina ganhou!!!')

elif jokepo == 'PAPEL':
    print("Voçê consegui ganhar da SKYNET")