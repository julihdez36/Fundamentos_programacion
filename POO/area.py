# Hallar el area de un triángulo

def area_traingulo(base,altura):
    return (base*altura)/2


base = float(input('Ingresa la base del triangulo: '))
altura = float(input('Ingresa la altura del triangulo: '))

a = area_traingulo(base,altura)

print(f'El area del triangulo de altura {altura} y base {base} es: {a}')
    

