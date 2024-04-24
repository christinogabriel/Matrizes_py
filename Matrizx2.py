#Faça um programa que preencha uma matriz 3x3 com números inteiros e multiplique todos os seus valores por 2. Apresente ambas matrizes

matrizEntrada = [[0]*3 ,[0]*3, [0]*3]
matrizSaida = [[0]*3 ,[0]*3, [0]*3]

for row in range(3):
    for col in range(3):
        matrizEntrada[row][col] = int(input(f'Entre com o valor [{row}][{col}] :'))
        matrizSaida[row][col] = 2 * matrizEntrada[row][col]

print()

print('Matriz Entrada')

for i in range(3):
    print(matrizEntrada[i])

print()

print('Matriz Saída')

for i in range (3):
    print(matrizSaida[i])


#----------------------------------------------------------------------
    

matrizEntrada = [[0]*3 ,[0]*3, [0]*3]
matrizSaida = [[0]*3 ,[0]*3, [0]*3]


for row in range(3):
    for col in range(3):
        matrizEntrada[row][col] = int(input(f'Entre com o valor [{row}][{col}]:'))
        matrizSaida[row][col] = 2 * matrizEntrada[row][col]

print()

print('Matriz Entrada')

for i in range(3):
    print(matrizEntrada[i])

print()

for i in range(3):
    print(matrizSaida[i])
    