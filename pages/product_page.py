from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        #alert = self.browser.switch_to.alert
        self.solve_quiz_and_get_code()
        #alert.send_keys(self.solve_quiz_and_get_code())
        #alert.accept()

    def shoul_be_name_match_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text == self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_CART).text

    def should_be_prices_checked(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_OF_ITEM).text == self.browser.find_element(*ProductPageLocators.PRICE_OF_ITEM_IN_CART).text
