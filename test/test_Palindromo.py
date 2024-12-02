"""
Test creados por Victor Jiménez Guerrero
"""

import unittest
from app.charfun import esPalindromo


class TestEsPalindromo(unittest.TestCase):
    # Comprueba si las inputs son palindromos
    def test_es_palindromo(self):
        palindromos = [
            "abba",
            "a,b,a",
            "A man, a plan, a canal: Panama",
            "Was it a car or a cat I saw?",
            "121",
            "No 'x' in Nixon",
            "",
            " ",
            "a",
        ]
        for frase in palindromos:
            # De esta forma nos devuelve el valor del caso al fallar
            with self.subTest(frase=frase):
                self.assertTrue(esPalindromo(frase))
                
    # Comprueba si las inputs no son palindromos
    def test_no_es_palindromo(self):
        no_palindromos = [
            "abca", 
            "a,c,d", 
            "race a car", 
            "tab a cat",
            "vjimgue"
        ]
        for frase in no_palindromos:
            # De esta forma nos devuelve el valor del caso al fallar
            with self.subTest(frase=frase):
                self.assertFalse(esPalindromo(frase))
    
    # Comprueba que devuelva una excepción si el tipo de la variable de entrada no es una string
    def test_excepcion_tipo_incorrecto(self):
        lista_type_errors = [
            12, 
            [1, 2, 4], 
            (1, 3, 5), 
            1.3, 
            {"vjimgue": 3, "1": 5, 4: 6}
        ]
        for error in lista_type_errors:
            # De esta forma nos devuelve el valor del caso al fallar
            with self.subTest(caso=error):
                with self.assertRaises(TypeError):
                    print(error)
                    esPalindromo(error)


if __name__ == "__main__":
    unittest.main()