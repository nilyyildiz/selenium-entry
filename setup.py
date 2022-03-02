from selenium import webdriver

chrome_driver_path = "C:/Users/nilyy/OneDrive/Masaüstü/drivers/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path) 

driver.get("https://www.sadikturan.com")