# Faça um programa que identifique o ano de nascimento de uma pessoa a partir da idade e do ano atual

ano_atual = int(input('Digite o ano atual: '))
idade = int(input('Quantos anos você completou/completará esse ano? '))
ano_nasc = ano_atual - idade
print(f'Você nasceu em {ano_nasc} correto?')