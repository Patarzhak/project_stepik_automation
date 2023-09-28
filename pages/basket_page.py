from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_cart_empty(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
       "The cart was not empty"

    def should_be_message_empty_cart(self):
        assert not(self.is_not_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE)), \
       "Empty cart message no"