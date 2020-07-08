from selenium.webdriver.common.by import By
from selenium import webdriver


class HomePage:
    fromCity =(By.ID,"fromCity")
    #self.driver.find_element_by_id("fromCity")
    entertext=(By.CSS_SELECTOR,"input[placeholder='From']")
    autodropdown=(By.CSS_SELECTOR,"p[class*='blackText']")

    def __init__(self,driver):
        self.driver=driver
    def fromCityFun(self):
        return self.driver.find_element(*HomePage.fromCity)

    def enterTextFun(self):
        return self.driver.find_element(*HomePage.entertext)

    def autodropdownFun(self):
        return self.driver.find_elements(*HomePage.autodropdown)