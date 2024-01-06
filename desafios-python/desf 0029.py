km = float(input('Valor que o carro passou?? '))

if km > 80: #condiçao simples
    print('Você acabou de levar uma muta Parabrens!')
    km2 = float((km - 80) * 7.00)
    print('O valor da muta ficou em {:.2f}'.format(km2))
print('Sua calma te livrou de levar uma muta bem cara')
