al = float(input('Digite sua altura: '))
ps = float(input('Digite seu peso em kg: '))
imc = ps / al
if imc <= 18.5:
    print('Voçê esta a baixo do peso')
elif 18.5 < imc and imc  > 25:
    print('Voçê esta no peso ideal')
elif 25 > imc and imc < 30:
    print('Voçê esta a sobrepeso')
elif 30 > imc and imc < 40:
    print('voçê esta com obesidade')
elif imc > 40 :
    print('Voçê esta com obesida morbida ')
print('fim programa')

