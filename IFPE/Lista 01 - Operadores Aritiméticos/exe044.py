# Receba a altura do degrau de uma escada e a altura que o usuario deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir o seu ojetivo

degrau = float(input('Qual a altura do seu degrau em cm? '))
altura = float(input('Qual altura você deseja subir em m? '))
qtd_degraus = altura / (degrau / 100)
print(f'Para subir {altura:.2f} m de altura, é necessário subir {qtd_degraus} degraus.')