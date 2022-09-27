def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    x=3
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + x) % 26) + 65
        if (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + x) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

claroCESAR = 'VENI VIDI VINCI ZETA'
print(claroCESAR)
print("Cifro")
cifradoCESAR = cifradoCesarAlfabetoInglesMAY(claroCESAR) 
print(cifradoCESAR)

def desCifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    x=3
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = 0
        ordenCifrado = ord(cadena[i])
        # Cambia el caracter a cifrar
        if (ordenCifrado >= 65 and ordenCifrado <= 90):
            ordenClaro = (((ordenCifrado - 65) - x) % 26) + 65
        if (ordenCifrado >= 97 and ordenCifrado <= 122):
            ordenClaro = (((ordenCifrado - 97) - x) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenClaro)
        i = i + 1
    # devuelve el resultado
    return resultado

print("Descifro")
claroCESAR = desCifradoCesarAlfabetoInglesMAY(cifradoCESAR) 
print(claroCESAR)
