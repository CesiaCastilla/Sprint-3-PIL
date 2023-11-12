from functions.functions import Functions
from functions.Inicializar import Inicializar
import unittest
import time
from selenium import webdriver

class Test_002(unittest.TestCase, Functions):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        self.driver.maximize_window() 
        self.driver.get("https://shop.thonet-vander.com/")
        time.sleep(2)

    def test_002(self):
        Functions.get_json_file(self, "Thonet_vander")
        
        """Validar link de login Iniciar Sesión"""
        iniciarSesion = Functions.get_elements(self, "IniciarSesion")
        self.assertTrue(iniciarSesion, "El link 'Iniciar sesión' no se encontró")
        iniciarSesion.click()
        print("Se redirige a la página de login correctamente")
        self.driver.save_screenshot('../data/evidencia/captura-tst_02.png')
        
        """Validar campo E-Mail"""
        Email = Functions.get_elements(self, "Email")
        self.assertTrue(Email, "El elemento 'Email' no se encontró")
        self.assertTrue(Email.is_enabled(), "El elemento Email no está habilitado")
        Email.send_keys(Inicializar.User)
        
        """Validar campo Contraseña"""
        Password = Functions.get_elements(self, "Password")
        self.assertTrue(Password, "El elemento Password no se encontró")
        self.assertTrue(Password.is_enabled(), "El elemento Password no está habilitado")
        Password.send_keys(Inicializar.Password)
        
        """Validar botón INGRESÁ"""
        Ingresar = Functions.get_elements(self, "Ingresar")
        texto_boton = Ingresar.text
        boton_esperado = "INGRESÁ"
        self.assertEqual(texto_boton, boton_esperado, f"El botón ({texto_boton}) no se encuentra ({boton_esperado})")
        print("El botón es visible")
        time.sleep(3)
        
        Ingresar = Functions.get_elements(self, "Ingresar")
        self.assertTrue(Ingresar, "El elemento 'Botón ingresar' no se encontró")
        Ingresar.click()
        print("Se inicia sesión correctamente y se redirige a la home")
        time.sleep(3)
        
        """Validar usuario ya logueado"""
        Usuario = Functions.get_elements(self, "Usuario")
        self.assertTrue(Usuario, "El link 'Hola, cc' no se encontró")
        Usuario.click()
        print("Se redirige a la página de los datos del Usuario correctamente")
        time.sleep(3)
        
        """Validar Datos Generales del usuario"""
        Datos_Generales = Functions.get_elements(self, "DatosGenerales")
        texto_Datos_Generales = Datos_Generales.text
        datos_esperados = "Datos Generales"
        self.assertEqual(texto_Datos_Generales, datos_esperados, f"La info de los datos generales ({texto_Datos_Generales}) no se encuentra ({datos_esperados})")
        print("Los Datos Generales del usuario son visibles")
        self.driver.save_screenshot('../data/evidencia/captura-tst_002.png')
        time.sleep(3)
        
        """Validar link Thonet & Vander"""
        Thonet_Vander = Functions.get_elements(self, "Thonet_vander")
        self.assertTrue(Thonet_Vander, "El elemento 'Thonet & Vander' no se encontró")
        Thonet_Vander.click()
        print("Se redirige a la Home correctamente")
        self.driver.save_screenshot('../data/evidencia/captura-tst_0002.png') 
        
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()