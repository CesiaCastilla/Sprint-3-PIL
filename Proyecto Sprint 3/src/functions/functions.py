from functions.Inicializar import Inicializar
import pytest
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class Functions(Inicializar):
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        if navegador == "CHROME":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            return self.driver
    def __init__(self):
        self.json_GetFieldBy = None
        self.json_ValueToFind = None
    
    def get_json_file(self, file):
        """para abrir el archivo"""
        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                return self.json_strings
        except FileNotFoundError:
                print("get_json_file: " + json_path)
                self.json_strings = False
                Functions.tearDown(self)
                pytest.skip("get_json_file: No se encontro el Archivo " + file)
            
    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para este TC")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError: 
                self.msj = "get_entity: No se encontro la key a la cual se hace referencia: " + entity
                Functions.tearDown(self, "fail")
                pytest.skip(self.msj)
       
    def get_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)
        
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "xpath":
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.LINK_TEXT, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "class":
                    elements = self.driver.find_element(By.CLASS_NAME, self.json_ValueToFind)
                
                return elements
            except AttributeError:
                self.msj = ("get_elements AttributeError: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except NoSuchElementException:
                self.msj = ("get_elements NoSuchElementException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                self.msj = ("get_elements TimeoutException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except UnexpectedAlertPresentException as e:
                self.msj = "get_elements: " + str(e)
                Functions.tearDown(self)
        
    def tearDown(self): #Pasamos a este archivo, el tearDown de los TCs
        self.driver.quit()
        