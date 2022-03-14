# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
print('Insira as medidas da sua parede, em metros, para saber quantos litros de tinta serão necessários para pintá-la')
b = float(input('Largura: '))
h = float(input('Altura: '))
a = b * h
litros = a / 2
print('Sua parede possui uma área de {}m², portanto serão necessários {} L de tinta para pintá-la.'.format(a, litros))