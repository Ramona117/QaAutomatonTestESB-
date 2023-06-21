from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.implicitly_wait(10)  # Implicit wait for 10 seconds

driver.get("https://www.saucedemo.com/")

# Wrong username
username = driver.find_element(By.ID, "user-name")
username.send_keys("wrong_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
)
assert "Username and password do not match" in error_message.text

username.clear()
password.clear()

# Wrong password
username.send_keys("standard_user")
password.send_keys("wrong_password")
login_button.click()

error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
)
assert "Username and password do not match" in error_message.text

driver.quit()
