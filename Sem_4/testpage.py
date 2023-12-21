import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
from zeep import Client, Settings
import requests

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=testdata.get('path'), settings=settings)


def check_text(word):
    if not word:
        logging.exception("No word")
        return None
    try:
        return client.service.checkText(word)[0]['s']
    except:
        logging.exception(f"Exception while operation")
        return False


def get_post(token):
    get = requests.get(url=testdata['path_posts'], headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()
    else:
        logging.exception('Request error')


class TestSearchLocators:
    ids = dict()
    with open('./locator.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Sent {word} to element {element_name} ")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.info(f"Find text {text} in field {element_name}")
        return text

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description="password form")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME_FIELD'], word, description="contact name form")

    def enter_contact_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_MAIL_FIELD'], word, description="contact mail form")

    def enter_contact_text(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_TEXT_FIELD'], word, description="contact text form")

# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact button')

    def click_contact_button_send(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN_SEND'], description='contact button send')

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error text')

    def get_success_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SUCCESS_FIELD'], description='success text')

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

# CHECK TEXT
