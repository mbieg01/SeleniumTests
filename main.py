from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\MonikaBiegon\PycharmProjects\SeleniumTests\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
element = driver.find_element(By.CLASS_NAME, 'central-textlogo')
result = element.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[1]/h1/span')
driver.close()
