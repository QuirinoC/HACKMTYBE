from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException

import asyncio

import urllib.request 



class Browser(Chrome):
    def __init__(self, **kwargs):
        Chrome.__init__(self, **kwargs)

    def find_by_text(self, text):
        return self.find_element_by_xpath(f"//*[text()='text']")




driver = Browser(executable_path="/Users/Quirino/Desktop/hackmty/HACKMTYBE/chromedriver")

URL = "http://www.dermnet.com/dn2/allJPG3/"

driver.get(URL)

DISEASES = {
    'Psoriasis' : [],
    'Hives' : [],
    'Acne' : [],
    'Atopic' : [],
    'Melanoma' : [],
    'Basal' : []
}

DATA_FOLDER = 'disease_data/'

c = 0

async def store_img(url: str, path: str):
    urllib.request.urlretrieve(url, path)

line_data = driver.find_elements_by_tag_name('a')[c:]
print("line data done")
#input("Continue:")

request_stack = []

for line in line_data:
    for disease in DISEASES.keys():
        if disease in line.text or disease.lower() in line.text:
            async_req = store_img(URL+line.text, DATA_FOLDER + disease + "/" + line.text)
            request_stack.append(async_req)

    if c % 100 == 0:
        print(c)
    c+=1


driver.close()