km = float(input('Qual e a distancia a percorrer na viagem?'))

'''
preço = km *0.50 if km <= 200 else km * 0.45
print('O preço da passagem e de {}'.format(preço))
'''
if km <= 200:
    print('O valor da sua viagem de {}km foi de {:.2f}'.format(km, km * 0.50))
else:
    print('O valor da sua viagem de {}km foi de {:.2f}'.format(km, km * 0.45))
