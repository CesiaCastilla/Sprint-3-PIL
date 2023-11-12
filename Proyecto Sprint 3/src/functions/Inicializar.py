import os

class Inicializar():
    """Directorio Base"""
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    """es para que suba al nivel de src / os.path nos busca la ubicación absoluta de nuestro directorio base"""

    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    """JsonData"""
    Json = basedir + "/Pages"
    
    Environment = 'Dev'
    # BROWSER DE PRUEBAS
    NAVEGADOR = 'CHROME'
    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'
    
    Excel = basedir + '/data/DataTest.xlsx'
    if Environment == 'Dev':
        URL = "https://shop.thonet-vander.com/"
        User = "123@gmail.com"
        Password = "1234"
