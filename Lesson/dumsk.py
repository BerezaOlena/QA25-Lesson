#https://www.dumskaya.net/


from factory.new_user import User
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
import os
import time

my_user = User()
options = ChromeOptions()
foptions = FireFoxOptions()
options.headless = False #True Запуск теста без включения браузера

path = f'{os.getcwd()}/drivers/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
url = 'https://www.dumskaya.net/'

driver.maximize_window()
driver.get(url)

xpath_enter_button = '//a[@id="pp"]/b'
xpath_enter_registration_button = '//a[@href="/register/"]'

xpath_register_email = '//td/input[@name="email"]'
xpath_register_nick = '//input[@name="nick"]'
xpath_register_password = '//input[@name="password1"]'
xpath_register_password2 = '//input[@name="password2"]'
xpath_register_gender_male = '//input[@name="gender"][@value="m"]'
xpath_register_gender_female = '//input[@name="gender"][@value="f"]'
xpath_register_button = '//input[@type="submit"]/following::input[@type="submit"]' # XPath Axis ось XPath

xpath_user_finish = '//a[@class="celluname1"]'


enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
enter_button.click()
enter_registration_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
enter_registration_button.click()
# email = 'qwerty1qwerty1@gmail.com' #'qwerty1@gmail.com'
# nick = 'qwerty1qwerty1' #'qwerty1'
# password = 'qazxsw111qwerty1qwerty1' #'qazxsw111'
register_email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_email)))
register_email_field.send_keys(my_user.email)

register_nick_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_nick)))
register_nick_field.send_keys(my_user.nick)

register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password)))
register_password.send_keys(my_user.password)

register_password2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password2)))
register_password2.send_keys(my_user.password)

register_gender_male = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_gender_male)))
register_gender_male.click()

register_gender_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_button)))
register_gender_button.click()

time.sleep(500)