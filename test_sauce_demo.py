from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Tell Chrome to run in invisible mode (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start the browser
driver = webdriver.Chrome(options=chrome_options)

# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(1)  # wait for the page to load

# 🧪 Test Case 1: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "inventory" in driver.current_url:
    print("✅ Test Case 1 Passed: Logged in!")
else:
    print("❌ Test Case 1 Failed: Couldn't login.")

# 🧪 Test Case 2: Add item to cart
driver.find_element(By.CLASS_NAME, "btn_inventory").click()
time.sleep(1)

cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
if cart_count == "1":
    print("✅ Test Case 2 Passed: Item added to cart!")
else:
    print("❌ Test Case 2 Failed: Item not added.")

# 🧪 Test Case 3: Checkout with empty cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Remove the item
driver.find_element(By.CLASS_NAME, "cart_button").click()
time.sleep(1)

# Try to checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)

if "checkout-step-one" in driver.current_url:
    print("❌ Test Case 3 Failed: Checked out with empty cart!")
else:
    print("✅ Test Case 3 Passed: Checkout blocked on empty cart.")

# Close the browser
driver.quit()
