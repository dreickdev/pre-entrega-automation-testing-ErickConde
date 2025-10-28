from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Localizadores de la página de Login"""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
class InventoryPageLocators:
    """Localizadores de la página de Inventario (Productos)"""
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    FIRST_ITEM_NAME = (By.XPATH, "(//div[@class='inventory_item_name'])[1]")
    # ------------------------------------------------

    FIRST_ITEM_PRICE = (By.XPATH, "(//div[@class='inventory_item_price'])[1]")
    ADD_TO_CART_FIRST_ITEM = (By.XPATH, "(//button[text()='Add to cart'])[1]")

class CartPageLocators:
    """Localizadores del Carrito y Header"""
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")