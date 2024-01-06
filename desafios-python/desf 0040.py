nt1 = float(input('Sua peimeira nota: '))

nt2 = float(input('Sua segunda nota: '))

ntf = (nt1 + nt2) / 2
print(ntf)
if ntf < 5.0:

    print('Você esta de Reprovado')

elif ntf <= 6.9:

    print('Você esta de Recuperação')

elif ntf >= 7.0:

    print('Você foi aprovado Parabrens')

print('Tenha um otimo dia')
