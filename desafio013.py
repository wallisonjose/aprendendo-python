# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento 
print('Os salários terão 15% de aumento, informe quanto você ganha abaixo e veja o novo valor com o reajuste')
vi = float(input('Insira seu salário atual: R$'))
vf = vi*1.15
print('Seu salário após o reajuste será de: R${:.2f}'.format(vf))