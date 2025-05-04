# Suma de Gauss

n = int(input('Ingrese un número límite: '))

suma = 0
i = 1

while i<=n:
    suma = suma + i 
    i = i + 1

print(f'La suma de los número enteros hasta {n} es {suma}')


