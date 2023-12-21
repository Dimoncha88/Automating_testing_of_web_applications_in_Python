from testpage import OperationsHelper
import logging
import yaml
import time
from testpage import check_text, get_post

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step_2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(testdata['sleep_time'])
    testpage.enter_contact_name('Test')
    testpage.enter_contact_mail('test@test.ru')
    testpage.enter_contact_text('Some text')
    testpage.click_contact_button_send()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_alert_text() == f'{testdata["alert_text"]}'


def test_step_4_check_text(good, bad):
    logging.info("Test4 starting")
    try:
        assert good in check_text(bad)
    except TypeError:
        logging.exception(f"Exception while operation, enter a new word")
        return False


def test_step_5_check_post(token):
    logging.info("Test5 starting")
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert testdata['id_check'] in res
