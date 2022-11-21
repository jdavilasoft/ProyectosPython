#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : jdavila.soft@gmail.com
# Created Date: 21.11.22
# version ='1.0'
# ---------------------------------------------------------------------------
# 
''' https://www.freecodecamp.org/espanol/news/11-proyectos-de-python-que-los-desarrolladores-junior-pueden-crear-para-practicar/
'''
# ---------------------------------------------------------------------------

print("Bienvenido, vamos a calcular si un numero es par o impar")
num = int(input("En que numero estas pensando? (0 - 1000): "))

if (0 <= num <= 1000):
    if num % 2 == 0:
        print("Es un numero PAR")
    else:
        print("Es un numero IMPAR")
    print("Puedes validar otro numero")
else:
    print("Numero no valido")