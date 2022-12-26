
frase_original = '''
    El mar es inmenso,
    el desierto infinito,
    pero estar contigo,
    es lo mas bonito.
    '''

agua = input('Ingresa una fuente de agua: ')
desierto = input('Ingresa un lugar: ')
contigo = input('Ingresa un preposion y/o pronombre: ')
bonito = input('Ingresa un adjetivo: ')

frase_usr = f'''
    El {agua} es inmenso,
    el {desierto} infinito,
    pero estar {contigo},
    es lo mas {bonito}.
    '''

print(frase_usr)