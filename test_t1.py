#guvi.in
# guvi.in/signin
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.fixture
def setup():
   driver = webdriver.Chrome()
   driver.maximize_window()
   yield driver
   driver.quit()


def test_switch_between_tabs(setup):
   driver = setup
   #open https://www.guvi.in
   driver.get("https://www.guvi.in")
   print("Guvi Opened")
   time.sleep(5)


   #guvi/signin
   driver.execute_script("window.open('https://www.guvi.in/sign-in/')")
   time.sleep(5)


   #get all window handles
   windows = driver.window_handles


   driver.switch_to.window(windows[0])
   print("switched to guvi")
   time.sleep(5)


   driver.switch_to.window(windows[1])
   print("switched to guvi/signin")
   time.sleep(5)


def test_guvi(setup):
    driver = setup
    driver.get('https://www.guvi.in/sign-in/')
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("surbh@gmail.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("XXXXX")
    login = driver.find_element(By.ID, "login-btn")
    login.click()

    time.sleep(5)


    driver.quit()










