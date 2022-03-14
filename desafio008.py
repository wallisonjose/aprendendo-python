# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
v = float(input('Digite o valor em metros para que possamos convertê-lo: '))
vcm = v*100
vmm = v*1000
print('Esse valor vale:\nEm centímetros: {}\nEm mimímetros: {}\n'.format(vcm, vmm))