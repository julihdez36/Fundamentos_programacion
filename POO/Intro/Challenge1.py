'''
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)
    
palabra1 = input('Escribe la primera palabra: ')
palabra2 = input('Escribe la segunda palabra: ')


if anagramas(palabra1, palabra2):
    print(f'Las palabras {palabra1} y {palabra2} son anagramas')
else: print(f'Las palabras {palabra1} y {palabra2} son anagramas')


