from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.TAG_NAME, "h1")
    NAME_OF_PRODUCT_IN_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_OF_ITEM_IN_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_OF_ITEM = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH,"//*[@id='messages']/div[1]/div")