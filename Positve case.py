from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.implicitly_wait(10) 

driver.get("https://www.saucedemo.com/")

#Login
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

inventory_title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "title"))
)

#Add item to the cart
add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
add_to_cart_button.click()

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

checkout_button = driver.find_element(By.XPATH, "//button[text()='CHECKOUT']")
checkout_button.click()

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Ramandha")
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Fadilla")
postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("21223")

continue_button = driver.find_element(By.XPATH, "//input[@value='CONTINUE']")
continue_button.click()

finish_button = driver.find_element(By.XPATH, "//button[text()='FINISH']")
finish_button.click()

order_complete_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
)

assert "THANK YOU FOR YOUR ORDER" in order_complete_text.text

driver.quit()
