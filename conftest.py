import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    Service = Service(ChromeDriverManager().install())
    navedador = webdriver.Chrome(service=Service)
    navedador.implicitly_wait(5)
    yield navedador
    print=("Cerrando el navegador..")
    navedador.quit()