from math import cos, sin, tan, radians
an = float(input('Qual e o angulo: '))
print('O cosseno do numero {} sera {:.2f}'.format(an, cos(radians(an))))
print('O seno do nuemro {} sera {:.2F}'.format(an, sin(radians(an))))
print('A tangente do numero {} sera {:.2f}'.format(an, tan(radians(an))))
