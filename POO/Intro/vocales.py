# Calcular el numero de vocales de una frase

frase = str(input('Frase: ')).lower()
vocales = 'aeiou'
contador = 0

for i in frase:
    if i in vocales:
        contador += 1
    
print(f'Su frase tiene {contador} vocales')