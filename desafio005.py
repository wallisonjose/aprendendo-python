# Crie um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor 
n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1 
print('O antecessor de {} é: {} \nO sucessor de {} é: {}'.format(n, ant, n, suc))