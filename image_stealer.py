from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException



class Browser(Chrome):
    def __init__(self, **kwargs):
        Chrome.__init__(self, **kwargs)

    def find_by_text(self, text):
        return self.find_element_by_xpath(f"//*[text()='text']")




driver = Browser(executable_path="/Users/Quirino/Desktop/hackmty/HACKMTYBE/chromedriver")

driver.get("http://www.dermnet.com/dn2/allJPG3/")

DISEASES = {
    'Psoriasis' : [],
    'Hives' : [],
    'Acne' : [],
    'Atopic' : [],
    'Melanoma' : [],
    'Basal' : []
}

line_data = driver.find_elements_by_tag_name('a')

c = 0
for line in line_data:
    print('here')
    for disease in DISEASES.keys():
        if disease in line.text:
            DISEASES[disease].append(line)
            if c == 100:
                c =0
                print(line.text)
            c += 1

driver.close()