from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup: Headless Chrome for Codespaces
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    # 🔗 Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # 🧪 Test Case 1: Login with valid credentials
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory"))
    print("✅ Test Case 1 Passed: Logged in successfully!")

    # 🧪 Test Case 2: Add item to cart
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))).click()

    cart_count = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    if cart_count == "1":
        print("✅ Test Case 2 Passed: Item added to cart!")
    else:
        print("❌ Test Case 2 Failed: Cart count mismatch.")

    # 🧪 Test Case 3: Try to checkout with empty cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_button"))).click()  # Remove item
    time.sleep(1)  # Just a small buffer for DOM update

    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)  # Again, allow URL update

    if "checkout-step-one" in driver.current_url:
        print("❌ Test Case 3 Failed: Allowed checkout with empty cart!")
    else:
        print("✅ Test Case 3 Passed: Checkout blocked as cart is empty.")

except Exception as e:
    print(f"⚠️ Error during test execution: {e}")

finally:
    driver.quit()
