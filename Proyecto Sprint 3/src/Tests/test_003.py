from functions.functions import Functions
import unittest
import time
from selenium import webdriver

class Test_003(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        self.driver.maximize_window() 
        self.driver.get("https://shop.thonet-vander.com/")
        time.sleep(2)

    def test_003(self):
        Functions.get_json_file(self, "Thonet_vander")
        
        """Validar link Ofertas"""
        Ofertas = Functions.get_elements(self, "Ofertas")
        texto_Ofertas = Ofertas.text
        link_esperado = "Ofertas"
        self.assertEqual(texto_Ofertas, link_esperado, f"El botón ({texto_Ofertas}) no se encuentra ({link_esperado})")
        print("El link Ofertas es visible")
        time.sleep(3)
        
        Ofertas = Functions.get_elements(self, "Ofertas")
        self.assertTrue(Ofertas, "El link 'Ofertas' no se encontró")
        Ofertas.click()
        print("Se redirige a la página de ofertas correctamente")
        time.sleep(3)
        
        """Validar mensaje ¡Lo sentimos! No se encontraron productos disponibles por el momento."""
        sin_Resultados = Functions.get_elements(self, "SinResultados")
        texto_Sin_Resultados = sin_Resultados.text
        mensaje_esperado = "¡Lo sentimos! No se encontraron productos disponibles por el momento."
        self.assertEqual(texto_Sin_Resultados, mensaje_esperado, f"La info de la sucursal ({texto_Sin_Resultados}) no se encuentra ({mensaje_esperado})")
        print("El mensaje es visible.")
        time.sleep(3)
        self.driver.save_screenshot('../data/evidencia/captura-tst_003.png')
        
        """Validar link Thonet & Vander"""
        Thonet_Vander = Functions.get_elements(self, "Thonet_vander")
        self.assertTrue(Thonet_Vander, "El elemento 'Thonet & Vander' no se encontró")
        Thonet_Vander.click()
        print("Se redirige a la Home correctamente")
        self.driver.save_screenshot('../data/evidencia/captura-tst_0003.png') 
        
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()