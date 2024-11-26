r"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 21/11/2024
Autor. Gregorio Coronado Morón
Dependencias. Unicodedata
"""
import unicodedata
from app.palindromo import esPalindromo

def main():
    frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
    if frase.lower() == "salir":
        print("Programa finalizado.")
    else:
        # Comprobar si es palíndromo
        if esPalindromo(frase):
            print("La frase es palíndroma.")
        else:
            print("La frase no es palíndroma.")