frase = str(input('Digite um  frase:')).strip().upper()
print('A letra a aprace {}'.format(frase.count('A')))
print('A letra a pareceu primeiramente na posicao {}'.format(frase.find('A')+1))
print('A ultima posicao que a letra a apreceu foi {}'.format(frase.rfind('A')))
