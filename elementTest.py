from selenium import webdriver

chrome_driver_path = "C:/Users/nilyy/OneDrive/Masaüstü/drivers/chromedriver"

driver= webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org")


blog_times = driver.find_elements_by_css_selector(".blog-widget time")
blog_names = driver.find_elements_by_css_selector(".blog-widget li a")
blogs = {}

for i in range(len(blog_names)):
    blogs[i] = {
        "time": blog_times[i].text,
        "name": blog_names[i].text
    }

for time in blog_times:
    print(time.text)

for name in blog_names:
    print(name.text)

print(blogs)



driver.close()