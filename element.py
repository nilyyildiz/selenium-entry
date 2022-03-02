from selenium import webdriver

chrome_driver_path = "C:/Users/nilyy/OneDrive/Masaüstü/drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.n11.com/urun/casio-edifice-ef-539d-1a2vfd-erkek-kol-saati-579233?magaza=gundogdusaat&recId=kwfgn7xm-2rdx4qgjglz-S.W_HOME_INT.AB.OLD-0vgwsro")

title = driver.find_element_by_class_name("proName").text
price=driver.find_element_by_class_name("newPrice").find_element_by_tag_name("ins").text
searchInput= driver.find_element_by_id("searchData")

print(title)
print(price)
print(searchInput)

driver.close()