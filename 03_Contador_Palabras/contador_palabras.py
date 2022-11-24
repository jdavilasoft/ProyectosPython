frase = input("Hola, en que estas pensando?")

lista = frase.split()

x = 0
for word in lista:
    x += 1

print('¡Muy bien, tu me has mostrado tu pensamiento en,', x, 'palabras!')