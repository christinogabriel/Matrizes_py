matriz1 =[[0]*3, [0]*3 , [0]*3]
matriz2 = [[0]*3, [0]*3 , [0]*3]

for i in range(3):
    for j in range (3):
        matriz1[i][j]=  int(input('Entre com um valor {i}{j} :'))
        matriz2[i][j] = matriz1[i][j] *2

print('MATRIZ 1')
for i in range (3):
    print(matriz1[i])

print()

print('MATRIZ 2')

for i in range (3):
    print(matriz2[i])