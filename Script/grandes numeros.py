# 100 Numpy exercise

import numpy as np
import matplotlib.pyplot as plt

def moneda(n_tiradas):
    opciones = ['cara', 'sello']
    resultados = np.random.choice(opciones, n_tiradas)
    return resultados

# Simular 10000 tiradas para una mejor visualización
n_tiradas = 10000
tiradas = moneda(n_tiradas)

# Convertir los resultados a valores numéricos (1 para 'cara', 0 para 'sello')
caras_numerico = np.where(tiradas == 'cara', 1, 0)

# Calcular el número de caras acumuladas y las probabilidades acumuladas
caras_acumuladas = np.cumsum(caras_numerico)
probabilidad_acumulada = caras_acumuladas / np.arange(1, n_tiradas + 1)


# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar la probabilidad acumulada
ax.plot(probabilidad_acumulada, label='Probabilidad acumulada de obtener una cara')

# Agregar una línea horizontal en 0.5 para referencia
ax.axhline(0.5, color='r', linestyle='--', label='Valor teórico (0.5)')

# Añadir títulos y etiquetas
ax.set_title('Convergencia de la probabilidad de una moneda')
ax.set_xlabel('Número de tiradas')
ax.set_ylabel('Probabilidad acumulada')
ax.set_ylim(0, 1) # Asegurar que el eje Y va de 0 a 1
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

# Mostrar la gráfica
plt.show()
