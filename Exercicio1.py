#Escreva um programa que rmazene 10 números inteiros em um vetor e exiba o maior e o menor valor armazenado


vetor = [0]*10 


for cont in range(10):
    vetor[cont] = int(input(f'Informe o valor da posição {cont}:'))
max = vetor[0] # assume, como base, que o primeiro numero é o maior

for cont in range (10): # vamos varrer o vetor, começando pelo [0]
    if vetor[cont] > max: # se o numero lido vetor [0] for maior que o max
        max = vetor[cont] # troca pelo numero lido
print(f'O maior Valor Informado foi {max}')


vetor = [0]*10

for cont in range(10):
    vetor[cont] = int(input(f'Iforme o Valor Da Posição : {cont}'))
max = vetor[0]

for cont in range(10):
    if vetor[cont] > max:
        max = vetor[cont]
print(f'O maior valor informado : {max}')


vetor = [0]*10

for cont in range(10):
    vetor[cont] = int(input(f'O valor da posção {cont}'))
max = vetor[0]

for cont in range (10):
    if vetor[cont] > max:
        max = vetor[cont]
print(f'O maior valor informado foi {max}')

vetor = 0* [10]

for cont in range (10):
    vetor[cont] = int(input(f'O valor da posição {cont}'))
max = vetor[0]

for cont in range(10):
    if vetor[cont] > max:
        max = vetor[cont]
print(f'O maior valor : {max}')