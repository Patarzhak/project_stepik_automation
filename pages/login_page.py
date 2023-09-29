from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators



class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM)


    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM)

