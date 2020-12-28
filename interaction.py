from selenium import webdriver

chrome_driver_path = "C:/Users/brian/Documents/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
stat = driver.find_element_by_css_selector("div#articlecount a")
stat.click()


# driver.quit()