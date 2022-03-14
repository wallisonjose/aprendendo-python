# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dòlares ela pode comprar. Considere o US$ 1,oo = R$ 3,27
v = float(input('Informe quantos Reais você possui e iremos informar quantos Dólares você pode adiquirir: R$ '))
vdol = v / 3.27
print('Com esse valor você pode comprar US${:.2f}'.format(vdol))