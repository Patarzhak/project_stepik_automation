from selenium.webdriver.common.by import By


class BasketPageLocators():
    CART_BUTTON = (By.XPATH, "//span/a[contains(text(), 'View basket')]")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_CART_MESSAGE = (By.XPATH,"//p[contains(text(), 'Your basket is empty')]")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD_INPUT2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR,"button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.TAG_NAME, "h1")
    NAME_OF_PRODUCT_IN_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_OF_ITEM_IN_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_OF_ITEM = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH,"//*[@id='messages']/div[1]/div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
