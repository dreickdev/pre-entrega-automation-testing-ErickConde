import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager 

@pytest.fixture(scope="function")
def driver():
    """
    Esta fixture crea y configura el driver de Firefox
    antes de cada test y lo cierra después.
    """
   
    service = Service(GeckoDriverManager().install())
    
    
    navegador = webdriver.Firefox(service=service) 
    
    navegador.implicitly_wait(5)
   
    yield navegador
    
    navegador.quit()