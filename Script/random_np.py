# Uso del random en numpy


import numpy as np
from numpy import random as rnd

rnd.random() # Return random floats in the half-open interval [0.0, 1.0)

rnd.randint(10,20,size = 10) # Return random integers from low (inclusive) to high (exclusive).


rnd.randint(10,20,10) + rnd.random() #Podemos sumar de esta manera, pero suma el mismo

rnd.randint(10,20,size = (10,10))

rnd.random((10,10)) # Return random floats in the half-open interval [0.0, 1.0). 


l = list(range(100)) #creamos una lista
rnd.choice(l,10) #Generates a random sample from a given 1-D array

# Esto es útil si quiero recoger muestras

l2 = ['José','Luis','Maria','Pedro','Lili']

rnd.choice(l2,3, replace = False)

# Ejemplo de una tirada de datos

def dado(n_lados = 6, n_tiradas = 1, n_dados = 1):
    s = list(range(1,n_lados+1))
    resultado = rnd.choice(s,(n_tiradas, n_dados))
    return resultado

dado(n_tiradas=10,n_dados = 3)

# También es posible ajustar probabilidades ocurrencia
# Esto es útil para hacer simulaciones experimentales
# Tipo cadenas de Markov

rnd.choice(['S','L','N'], p = [.2,.5,.3],size =100) # al final se definen intentos

# Podemos también modificar el orden de un arreglo

l = list(range(10))
l
rnd.shuffle(l) # Modify a sequence in-place by shuffling its contents.
l # this is the output

# Creemo un arrange y lo aleatorizaremos permutandolo
x = np.arange(0,1.01,0.01)
x

rnd.shuffle(x)
x

# También podemos hacerlo sin alterar el array original con permutation

rnd.permutation(x)

# Otros generadores de aleatorios

rnd.normal(loc = 0, scale = 1, size = 10) # N(10,1)

rnd.binomial(n = 100, p = .5, size = 100) #p numero de éxitos

rnd.poisson(lam = 10, size = (10000))


rnd.uniform(1,10,size = 100)

rnd.logistic(loc = 1, scale= 2, size = 100)

rnd.exponential(scale=1.0, size=100)

import seaborn as sns

x = rnd.normal(size = 1000)
sns.distplot(x);

x1 = rnd.binomial(100, p=.5, size = 100000)
sns.distplot(x1)

x2 = rnd.poisson(lam = 10, size = (10000)) #variar lambda
sns.histplot(x2)
