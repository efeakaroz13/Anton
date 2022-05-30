import selenium
from selenium import webdriver
import pyttsx3
import sys
import time

url = sys.argv[1]

driver = webdriver.Safari()
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
sentences = body_text.split(" ")
for s in sentences:
    time.sleep(0.1)
    try:
        my_elm = driver.find_elements_by_xpath("""//*[contains(text(),'"""+s.strip()+"""')]""")
        highlight(my_elm[0],0,"blue",2)
    except:
        pass