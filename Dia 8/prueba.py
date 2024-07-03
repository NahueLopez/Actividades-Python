"""
Esto es para probar el unittest que es para verificar si lo que importamos trae lo que necesitamos
tenemos que crear una class y entre parentecis unittest.TestCase y crear una funcion que comience con test
"""
import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.principal_mayuscula(palabra) #asignamos a resultado el return de la funcion
        self.assertEquals(resultado, "Buen Dia")    #De esta manera comprobamos si el resultado es igual a  lo que esperamos.

if __name__ == "__main__": #esta es la manera de que comience por el main
    unittest.main()


