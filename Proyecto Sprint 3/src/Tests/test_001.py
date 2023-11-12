from functions.functions import Functions
import unittest
import time
from selenium import webdriver

class Test_001(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        self.driver.maximize_window() 
        self.driver.get("https://shop.thonet-vander.com/")
        time.sleep(2)

    def test_001(self):
        Functions.get_json_file(self, "Thonet_vander")
        
        """Validar link Sucursales"""
        Sucursales = Functions.get_elements(self, "Sucursales")
        self.assertTrue(Sucursales, "El elemento 'Sucursales' se encontró")
        Sucursales.click()
        print("Se ingresa al link sucursales correctamente")
        
        """Validar información de Sucursales"""
        sucursal_CABA = Functions.get_elements(self, "SucursalCABA")
        texto_sucursal_CABA = sucursal_CABA.text
        sucursal_esperada = "C.A.B.A."
        self.assertEqual(texto_sucursal_CABA, sucursal_esperada, f"La info de la sucursal ({texto_sucursal_CABA}) no se encuentra ({sucursal_esperada})")
        print("La Sucursal CABA es visible.")
        self.driver.save_screenshot('../data/evidencia/captura-tst_001.png')
        time.sleep(2)
        
        """Validar link Thonet & Vander"""
        Thonet_Vander = Functions.get_elements(self, "Thonet_vander")
        self.assertTrue(Thonet_Vander, "El elemento 'Thonet & Vander' no se encontró")
        Thonet_Vander.click()
        print("Se redirige a la Home correctamente")
        self.driver.save_screenshot('../data/evidencia/captura-tst_0001.png')
        
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()