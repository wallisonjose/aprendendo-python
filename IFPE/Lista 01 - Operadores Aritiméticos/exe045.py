# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido

num = input('Digite um número inteiro positivo de 3 díigitos: ')
print(f'Número Lido = {num}')
print(f'Número Invertido = {num[::-1]}') #Tratamento de exibição das strings