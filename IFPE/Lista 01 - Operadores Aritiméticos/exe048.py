# Faça um programa que leia o horário (horas, minutos e segundos) de início e a duração em segundos de uma experiência biológica.  programa deve resultar com o novo horário de termino da experiência

horas = int(input('Informe as horas: '))
minutos = int(input('Informe os minutos: ')) 
segundos = int(input('Informe os segundos: '))
tempo_decorrido = int(input('informe o tempo decorrido do experimento(em segundos): '))

def converte_segundos(h, m, s):
  h = h*3600 #convertendo as horas para segundos
  m = m*60 #convertendo os minutos p/ segundos
  return h+m+s

tempo_convertido = converte_segundos(horas, minutos, segundos)

tempo_pos_exp = tempo_convertido + tempo_decorrido

new_hora = tempo_pos_exp//3600
resto = tempo_pos_exp%3600
new_minuto = resto//60
new_segundo = resto%60

print(f'Após passados os {segundos} segundos do experimento, ele terá acabado as {new_hora} horas, {new_minuto} minutos e {new_segundo} segundos')