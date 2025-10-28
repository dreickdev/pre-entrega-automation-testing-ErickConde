import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.locators import LoginPageLocators, InventoryPageLocators, CartPageLocators


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
 
def test_navegacion_catalogo(driver):
    """
    Prueba la navegación del catálogo.
    Criterios mínimos:
    - Valida título.
    - Valida presencia de productos.
    - Lista nombre/precio del primero.
    """

    driver.get(BASE_URL)
    driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    

    assert "Swag Labs" in driver.title, "El título 'Swag Labs' no se encontró"
    

    lista_de_productos = driver.find_elements(*InventoryPageLocators.INVENTORY_ITEMS)
    assert len(lista_de_productos) > 0, "No se encontraron productos en la página"
  
    nombre = driver.find_element(*InventoryPageLocators.FIRST_ITEM_NAME).text
    precio = driver.find_element(*InventoryPageLocators.FIRST_ITEM_PRICE).text
    
    print(f"\nINFO: Primer producto: {nombre}, Precio: {precio}")
    
    assert nombre != "", "El primer producto no tiene nombre"
    assert precio != "", "El primer producto no tiene precio"

def test_interaccion_carrito(driver):
    """
    Prueba añadir un producto al carrito.
    Criterios mínimos:
    - Agrega primer producto.
    - Verifica ítem en carrito (contador).
    - Navega al carrito y comprueba que esté allí.
    """
  
    driver.get(BASE_URL)
    driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
   
    driver.find_element(*InventoryPageLocators.ADD_TO_CART_FIRST_ITEM).click()
    
   
    contador = driver.find_element(*CartPageLocators.CART_BADGE).text
    assert contador == "1", "El contador del carrito no marcó '1'"
    
  
    driver.find_element(*CartPageLocators.CART_LINK).click()
    
 
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))
    

    items_en_carrito = driver.find_elements(*CartPageLocators.CART_ITEM)
    assert len(items_en_carrito) == 1, "El ítem no se añadió al carrito"