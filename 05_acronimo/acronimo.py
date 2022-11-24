frase = input("Hola, ingresa el nombre de tu organizacion: ")

lista = frase.split()

acro = ""
for word in lista:
    acro = acro + word[0].capitalize()

print('Tu acronimo es: ', acro)