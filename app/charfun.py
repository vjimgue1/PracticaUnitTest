"""
Función que verifica si una cadena es palíndroma.
Ignora espacios, mayúsculas y tildes.

Refactorizado por Victor Jiménez Guerrero
"""
def esPalindromo(cadena):
    # Comprobamos que la variable de entrada es una string
    if not isinstance(cadena, str):
        raise TypeError
    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

