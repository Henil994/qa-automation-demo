import time
from selenium.webdriver.common.by import By

def test_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    assert "Logged In Successfully" in driver.page_source
