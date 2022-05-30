import selenium
from selenium import webdriver
import pyttsx3
import sys
from bs4 import BeautifulSoup
import time

url = sys.argv[1]

driver = webdriver.Chrome("./chromedriver")
driver.get(url)
body_text = driver.find_element_by_tag_name('body').text
def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    xelem = element._parent
    def apply_style(s):
        xelem.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

print(body_text)
soup = BeautifulSoup(driver.page_source,"html.parser")
sentences = soup.find_all(["h1","p"])
for s  in sentences:

    try:
        my_elm = driver.find_elements_by_xpath("""//*[contains(text(),'"""+s.text.strip()+"""')]""")
        highlight(my_elm[0],2,"blue",2)
        print(s.text)
    except:
        pass