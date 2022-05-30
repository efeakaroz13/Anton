import selenium
from selenium import webdriver
import pyttsx3
import sys

url = sys.argv[1]

driver = webdriver.Safari()
driver.get(url)
body_text = driver.find_element_by_tag_name('body').text
driver.quit()
print(body_text)