from selenium import webdriver

chrome_driver_path = "C:/Users/brian/Documents/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")
menu = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
print(menu[1].text.split("\n"))
events = {}
x = 0
for event in menu:
    event_list = event.text.split("\n")
    date = event_list[0]
    name = event_list[1]

    events[x] = {"time":date, "name":name}
    x+=1
print(events)
driver.quit()