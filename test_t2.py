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


def test_guvi(setup):
    driver = setup
    driver.get('https://www.guvi.in/sign-in/')
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("surbhi1105520@gmail.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Avnisingh@2575")
    login = driver.find_element(By.ID, "login-btn")
    login.click()

    time.sleep(5)



def test_positive_login(setup):
    driver=setup
    driver.get("https://www.guvi.in/sign-in/")
    # Title and URL before login
    #assert driver.title == "Swag Labs"
    assert driver.current_url == "https://www.guvi.in/sign-in/"

    # Valid login
    driver.find_element(By.ID, "email").send_keys("surbhi1105520@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Avnisingh@2575")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(2)


    #assert "dashboard" in driver.current_url
    # After login
    #expected_dashboard_url = "https://www.guvi.in/courses/?current_tab=myCourses"
    #expected_title = "Swag Labs"
    html_content = driver.page_source
    # Save it as an .txt file (which you can open later in any browser)
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(html_content)
    #assert driver.current_url == expected_dashboard_url
    #assert driver.title == expected_title
    assert driver.current_url == "https://www.guvi.in/courses/?current_tab=myCourses"

    #print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)
    print("✅ Positive test passed: logged in successfully.")


def test_negative_login(setup):
    driver = setup
    driver.get("https://www.guvi.in/sign-in/")

    # Title and URL before login
    #assert driver.title == "Swag Labs"
    assert driver.current_url == "https://www.guvi.in/sign-in/"

    # ❌ Invalid login attempt
    driver.find_element(By.ID, "email").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(2)

    # Capture HTML content
    html_content = driver.page_source
    with open("Webpage_task_11_negative.txt", "w", encoding="utf-8") as file:
        file.write(html_content)

    # Still on the login page
    assert driver.current_url == "https://www.guvi.in/sign-in/"
   # assert driver.title == "Swag Labs"

    # Check for error message
    error_text = driver.find_element(By.CLASS_NAME, "invalid-feedback").text
    assert "Incorrect" in error_text

    #print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)
    print("❌ Negative test passed: login failed as expected.")