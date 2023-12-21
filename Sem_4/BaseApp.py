'''
Доработать проект так, как это было сделано в лекции:
добавить обработку ошибок
вынести локаторы в yaml-файл
добавить debug-логи
'''
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import requests

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    url = testdata['address']


def get_token():
    path = testdata['site_login']
    post = requests.post(url=path, data={'username': testdata['login'], 'password': testdata['password']})
    if post.status_code == 200:
            return post.json()['token']
    else:
        logging.exception('Request error')


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.driver.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f'Property {property} not found in element with {locator}')
        return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing
