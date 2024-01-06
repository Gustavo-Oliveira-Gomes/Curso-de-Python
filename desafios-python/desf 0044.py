f = str(input('Qual e a forma de paga mento: ')).upper()
parcela = str(input('caso seja no cartão digite se sera parcelado ou a vista caso nao cesa tecle n:')).upper()
pr = int(input('caso cartão digite o numero de parcelas  caso nao seja parcelado coloque 0: '))
pc = float(input('Preço do produto: '))

if f == 'CHEQUE' or f == 'DINHEIRO' and parcela == 'N':
    pcf =pc - pc * 0.10
    print('o valor ficou em {} com o desconto por ser em a vista recebeu desconto'.format(pcf))

elif f == 'CARTÃO' and parcela == 'VISTA':
    pcf =pc - pc * 0.05
    print('o valor sera de {} por ser a vista vc recebeu um desconto'.format(pcf))

elif f == 'CARTÃO' and parcela == "PARCELADO" and pr == 2:
    pcx = pc/ 2
    print('valor sera de {} parcelados em x2 o valor total sera {}'.format(pcx))

elif f == 'CARTÃO' and parcela == "PARCELADO" and 3 <= pr:
    pcf = pc + pc * 0.20
    pcx = pcf / pr
    print('o valor parcelado em {} sera de {} e o valor total ficou em {} '.format(pr, pcx, pcf))

else:
    print('error')