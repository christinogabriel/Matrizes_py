alunos = ['Ana', 'Joao', 'Carla', 'Aline', 'Pedro']
notas = [[10.0, 7.5, 4.3, 8.2, 6.0],[9.5, 8.0, 3.6, 7.8, 9.0], 
[6.5, 4.9, 5.7, 6.0, 7.2],[3.5, 1.0, 5.0, 3.6, 4.4],
[10.0, 9.0, 9.5, 8.9, 9.2]]


media = [0.0 ,0.0 ,0.0, 0.0 ,0.0]


for linha in range(5):
    somalinha = 0
    for coluna in range (5):
        somalinha = somalinha + notas[linha][coluna]

    media[linha]= somalinha/5

print(alunos)
print(media)

for i in range(5):
    if media[i] >= 6.0:
        mensagem = ' APROVADO !'
    else:
        mensagem = ' REPROVADO !'
print(f'{alunos[i]} está {mensagem}')