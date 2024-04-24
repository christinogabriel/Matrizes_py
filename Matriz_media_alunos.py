#Dada a matriz de alunos e notas, calcular a media de cada aluno e informar se ele passou (>=6) ou foi reprovado (<6)


alunos = ['Ana', 'Joao', 'Carla', 'Aline', 'Pedro']
notas = [ [10.0, 7.5, 4.3, 8.2, 6.0], [9.5, 8.0, 3.6, 7.8, 9.0],
           [6.5, 4.9, 5.7, 6.0, 7.2], [3.5, 1.0, 5.0, 3.6, 4.4],
           [10.0, 9.0, 9.5, 8.9, 9.2] ]
media = [0.0, 0.0, 0.0, 0.0, 0.0]

for row in range(5): # para cada linha (ou aluno)
  somaNotas = 0 # soma de notas de um aluno (linha i)
  for col in range(5):
    somaNotas = somaNotas + notas[row][col]
  media[i] = somaNotas / 5 # calcula media do aluno i

for row in range (5):
  if media[row] >= 6.0:
    msg = 'APROVADO'
  else:
    msg = 'REPROVADO'
  print(f'aluno {alunos[row]} tem média {media[row]:.1f} e está {msg}')