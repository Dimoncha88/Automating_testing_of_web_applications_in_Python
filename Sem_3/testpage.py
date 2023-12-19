from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_SUCCESS_FIELD = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    #Дорабатываем кнопку Contact us
    LOCATOR_CONTACT_BTN = (By.XPATH, '''// *[ @ id = "app"] / main / nav / ul / li[2] / a''')
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_CONTACT_MAIL_FIELD = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_CONTACT_TEXT_FIELD = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_CONTACT_BTN_SEND = (By.XPATH, '''//*[@id="contact"]/div[4]/button/span''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()


    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text


    def get_success_text(self):
        success_field = self.find_element(TestSearchLocators.LOCATOR_SUCCESS_FIELD, time=3)
        text = success_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_SUCCESS_FIELD[1]}")
        return text


    def click_contact_button(self):
        logging.info('Click Contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()


    def enter_contact_name(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)


    def enter_contact_mail(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_MAIL_FIELD[1]}")
        mail_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_MAIL_FIELD)
        mail_field.clear()
        mail_field.send_keys(word)


    def enter_contact_text(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_TEXT_FIELD[1]}")
        text_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_TEXT_FIELD)
        text_field.clear()
        text_field.send_keys(word)


    def click_contact_button_send(self):
        logging.info('Click Contact Us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN_SEND).click()


    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text
