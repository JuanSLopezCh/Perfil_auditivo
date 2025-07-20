from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Audeze LCD-1")
search.send_keys(Keys.RETURN)
time.sleep(3)

first_result = driver.find_element(By.CSS_SELECTOR, 'h2 a')
print("URL:", first_result.get_attribute('href'))