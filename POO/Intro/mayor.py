# Mayor que el anterior

valor = int(input('Cuántos valores va a introducir?'))

if valor < 1:
    print('ERROR')
else:
    while valor > 0:
        primero = int(input('escriba un numero: '))
        valor -=1
        numero = int(input('escriba un  numero mas grande que primero'))
        if numero <= primero:
            print('el numero no es masgrande que primero')
    print('gracias por su colaboración')
    