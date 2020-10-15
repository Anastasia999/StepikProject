from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url1 = self.browser.current_url
        assert "login" in current_url1, "Incorrect URL for login page"

    def should_be_login_form(self):
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.should_be_register_form(*LoginPageLocators.REGISTRATION_FORM),\
            "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        pswd_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PSWD1)
        pswd_field1.send_keys(password)
        pswd_field2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PSWD2)
        pswd_field2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION).click()
        success_alert = self.browser.find_element(*LoginPageLocators.SUCCESS_REGISTRATION_ALERT).text
        assert "Thanks for registering!" == success_alert, "Profile isn't created"





