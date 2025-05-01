import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.guvi.in/sign-in/')
    yield driver
    driver.quit()

def test_positive_login_fields_and_button(setup):
    driver = setup

    # Locate elements
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    # Validate fields and button are visible and enabled
    assert email_field.is_displayed() and email_field.is_enabled(), "Email input is not visible/enabled"
    assert password_field.is_displayed() and password_field.is_enabled(), "Password input is not visible/enabled"
    assert login_button.is_displayed() and login_button.is_enabled(), "Login button is not visible/enabled"

    # Enter valid credentials
    email_field.send_keys("surbhi1105520@gmail.com")
    password_field.send_keys("Avnisingh@2575")
    login_button.click()

    time.sleep(5)

    # Assert successful login by checking URL change or dashboard appearance
    assert "dashboard" in driver.current_url or "courses" in driver.current_url, "Login was not successful"


def test_negative_login_fields_and_button(setup):
    driver = setup
    driver.get('https://www.guvi.in/sign-in/')

    # Validate input fields and button are present, visible, and enabled
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "login-btn")

    assert email_field.is_displayed() and email_field.is_enabled(), "Email field is not ready"
    assert password_field.is_displayed() and password_field.is_enabled(), "Password field is not ready"
    assert submit_button.is_displayed() and submit_button.is_enabled(), "Submit button is not ready"

    # Attempt login with invalid credentials
    email_field.send_keys("invaliduser@example.com")
    password_field.send_keys("wrongpassword123")
    submit_button.click()

    time.sleep(5)  # Wait for login to process (you can use WebDriverWait for better practice)

    # Check that login fails by staying on the login page or showing an error
    current_url = driver.current_url
    assert "sign-in" in current_url, f"Expected to stay on login page, but URL is: {current_url}"

    # Optionally check for visible error message (update selector based on actual HTML)
    try:
        error_message = driver.find_element(By.CLASS_NAME, "error-message").text
        assert "Incorrect" in error_message or "invalid" in error_message.lower()
    except:
        print("No error message element found – please confirm selector.")
