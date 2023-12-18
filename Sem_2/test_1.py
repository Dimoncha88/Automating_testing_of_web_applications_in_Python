import time
import yaml

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


# def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
#     input1 = site.find_element('xpath', select_input_login)
#     input1.send_keys('test')
#     input2 = site.find_element('xpath', select_input_password)
#     input2.send_keys('test')
#     btn = site.find_element('css', select_input_button)
#     btn.click()
#     err_label = site.find_element('xpath', select_error)
#     assert err_label.text == '401'


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    assert answer.text == f'Hello, {testdata["login"]}'


def test_step_3_create_post(site, select_input_login, select_input_password, select_input_button, button_create_post,
                            select_title, select_description, select_content, button_save_post, select_user_post):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    create_btn = site.find_element('css', button_create_post)
    create_btn.click()
    time.sleep(testdata['sleep_time'])
    input_title = site.find_element('xpath', select_title)
    input_title.send_keys(testdata['title'])
    input_descript = site.find_element('xpath', select_description)
    input_descript.send_keys(testdata['description'])
    input_content = site.find_element('xpath', select_content)
    input_content.send_keys(testdata['content'])
    btn = site.find_element('css', button_save_post)
    btn.click()
    time.sleep(testdata['sleep_time'])
    answer = site.find_element('xpath', select_user_post)
    assert answer.text == f'{testdata["title"]}'
