from app.charfun import esPalindromo

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