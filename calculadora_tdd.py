import unittest


# Clase Calculadora
class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b

    def raiz_cuadrada(self, x):
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        aproximacion = x / 2.0
        while abs(aproximacion**2 - x) > 0.001:
            aproximacion = (aproximacion + x / aproximacion) / 2.0
        return aproximacion

    def exponencial(self, x):
        resultado = 1
        termino = 1
        n = 1
        while abs(termino) > 0.001:
            termino *= x / n
            resultado += termino
            n += 1
        return resultado


# Clase de Pruebas para Calculadora
class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(2, 3), 5)
        self.assertEqual(self.calc.suma(-1, 1), 0)
        self.assertEqual(self.calc.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(self.calc.resta(5, 3), 2)
        self.assertEqual(self.calc.resta(0, 5), -5)
        self.assertEqual(self.calc.resta(3, 3), 0)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplica(2, 3), 6)
        self.assertEqual(self.calc.multiplica(-1, 5), -5)
        self.assertEqual(self.calc.multiplica(0, 10), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, -1), -5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_raiz_cuadrada(self):
        self.assertAlmostEqual(self.calc.raiz_cuadrada(4), 2, places=3)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(9), 3, places=3)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), 1.414, places=3)
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-4)

    def test_exponencial(self):
        self.assertAlmostEqual(self.calc.exponencial(1), 2.718, places=3)
        self.assertAlmostEqual(self.calc.exponencial(0), 1, places=3)
        self.assertAlmostEqual(self.calc.exponencial(-1), 0.368, places=3)


# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
