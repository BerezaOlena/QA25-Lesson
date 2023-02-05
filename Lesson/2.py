# https://www.lingobest.com/free-online-english-course/

from factory.new_user import User
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
import time

my_user = User()

options = ChromeOptions()
options.headless = False  # True Запуск теста без включения браузера

path = f'{os.getcwd()}/drivers/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.lingobest.com/free-online-english-course/'

driver.maximize_window()
driver.get(url)

xpath_signup_button = '//span[@class="button__text"]' <span class="button__text">Зареєструватися</span>
xpath_register_email = '//input[@name="email"]'
xpath_register_username = '//input[@name="username"]'
xpath_register_password = '//input[@name="password"]'
xpath_user_create = '//span[@class="checkbox__icon checkbox__icon_state_multi"]'
xpath_user_create2 = '//span[@class="checkbox__icon checkbox__icon_state_multi"]'

enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_signup_button)))
enter_button.click()

register_email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_email)))
register_email_field.send_keys(my_user.email)

register_user_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_username)))
register_user_field.send_keys(my_user.nick)

register_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_register_password)))
register_password.send_keys(my_user.password)

register_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_user_create)))
register_button.click()

register_2button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_user_create2)))
register_2button.click()

time.sleep(500)

