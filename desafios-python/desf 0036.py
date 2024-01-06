# Teste para p imprestimo da casa
vlcs = float(input('Valor da casa? '))
slr = float(input('Qual e o valor do seu salario? '))
nq = int(input('Em quantos anos pretende pagar? '))
# calaculos
nm = nq * 12
nm2 = vlcs / nm
if nm2 > (slr * 30 / 100) - slr:
    print('O seu imprestimo foi aprovado')
elif nm2 < (slr * 30 / 100) - slr:
    print('O seu imprestimo nao foi aceito')
print('Tenha um bom dia')
