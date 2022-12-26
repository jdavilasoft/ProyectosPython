import random

numeroOculto = random.randint(1, 50)
veces = 1
print(numeroOculto)

miNumero = int(input("Ingresa un número [1-50]: "))

if miNumero not in range(1, 51):
    print("Numero no valido")
else:
    while miNumero != numeroOculto:
        if miNumero > numeroOculto:
            print("El numero oculto es menor")
        else:
            print("El numero oculto es mayor")

        miNumero = int(input("Ingresa otro número [1-50]: "))
        veces += 1

    print("Acertaste, intentaste", veces, "veces")