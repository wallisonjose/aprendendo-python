# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print('Somente hoje, todos os produtos etarão com 5% de desconto.')
v = float(input('Insira o valor do produto e veja seu valor com desconto: R$'))
vdesc = v*0.95
print('O produto saírá por: R${}'.format(vdesc))