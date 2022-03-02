from selenium import webdriver
import time

chrome_driver_path = "C:/Users/nilyy/OneDrive/Masaüstü/drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)
url="https://github.com"

driver.get(url)

time.sleep(1)

driver.maximize_window()
driver.save_screenshot("github.png")
print(driver.title) 

time.sleep(4)

driver.close()