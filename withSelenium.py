import selenium
from selenium import webdriver
import pyttsx3
import sys
from bs4 import BeautifulSoup
import time
import pyttsx3



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
sentences = body_text.split(".")

for s  in sentences:

    try:
        
        my_elm = driver.find_elements_by_xpath(f"""//*[contains(text(),"{s}")]""")
        

        
        
        xelem = my_elm[0]._parent
        def apply_style(s):
            xelem.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                my_elm[0], s)
        original_style = my_elm[0].get_attribute('style')
        apply_style("border: {0}px solid {1};".format("2", "blue"))
        #time.sleep(effect_time)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[37].id)
        engine.say(s)
        engine.runAndWait()
        
        apply_style(original_style)



        print(s)
    except Exception as e:
        print(e,s)
        