import unittest
from app.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    def test_es_palindromo(self):
        palindromos = ["abba", "a,b,a"]
        for frase in palindromos:
            self.assertTrue(esPalindromo(frase))
    
    def test_no_es_palindromo(self):
        no_palindromos = ["abca", "a,c,d"]
        for frase in no_palindromos:
            self.assertFalse(esPalindromo(frase))
            
    def test_excepcion_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            esPalindromo(12)
        with self.assertRaises(TypeError):
            esPalindromo([1,2,4])
        
        
            
if __name__ == "__main__":
    unittest.main()            