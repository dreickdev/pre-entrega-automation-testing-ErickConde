import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.locators import LoginPageLocators, InventoryPageLocators


BASE_URL = "https://www.saucedemo.com"

def test_login_exitoso(driver):
    """
    Prueba el login con credenciales válidas.
    Criterios mínimos:
    - Login automatizado con espera explícita.
    - Validación de /inventory.html.
    - Validación de "Products" y "Swag Labs".
    """
    driver.get(BASE_URL)

    driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
  
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )
    except:
      
        pytest.fail("El login falló o no redirigió a /inventory.html a tiempo")

   
    assert "Swag Labs" in driver.title, "El título 'Swag Labs' no se encontró"
    
    titulo_productos = driver.find_element(*InventoryPageLocators.PAGE_TITLE).text
    assert titulo_productos == "Products", "El título 'Products' no se encontró"