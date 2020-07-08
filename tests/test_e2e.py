import time

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self,setup):


        print(self.driver.current_url)
        self.driver.maximize_window()


        # Tried with javascriptexecutor... no use
        fromCity = self.driver.find_element_by_id("fromCity")
        #self.driver.execute_script("arguments[0].click();", fromCity)
        #self.driver.execute_script("arguments[0].click();", fromCity)

        ##pageobject implementation from homepage
        homepage=HomePage(self.driver)


        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB).click()
        action.perform()
        #action.move_to_element(fromCity).click().perform()
        action.move_to_element(homepage.fromCityFun()).click().perform()

        #self.driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
        homepage.enterTextFun().send_keys("del")

        time.sleep(2)

        #listCities = self.driver.find_elements_by_css_selector("p[class*='blackText']")
        listCities = homepage.autodropdownFun()

        print(listCities.__len__())
        print(len(listCities))

        # print(listCities)

        for city in listCities:
            print(city.text)
            if city.text == "Delta Junction, United States":
                city.click()
                print("I am clicked here....")
                time.sleep(5)
                break

#commenting here because we have already closed this driver in fixtures no need to close here... thats why its giving error
        #self.driver.close()

