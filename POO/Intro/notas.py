# Programa del promedio ponderado de tres notas

def promedio_ponderado(corte1,corte2,corte3):
    return corte1*0.3 + corte2*0.3+ corte3*0.4

corte = ['uno','dos','tres']
notas = []
for i in corte:
    nota = float(input(f'Ingrese la nota del corte {i}: '))
    notas.append(nota)

print(f'Sus notas son: \n Primer corte: {notas[0]} \n Segundo corte:   {notas[1]} \n Tercer corte: {notas[2]}')

promedio = promedio_ponderado(notas[0], notas[1], notas[2])

print(f'Su promedio ponderado es: {promedio}')
