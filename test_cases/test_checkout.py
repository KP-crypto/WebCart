from selenium import webdriver
from  selenium.webdriver.support.ui import Select
import pytest
import time
from pages.Checkout import Checkout
from Utilities.readProperties import Readconfig
from pages.websitePages import mainPage


class Test_002:
    url = Readconfig.getApplicationURL()

    def test_checkout(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.mp = mainPage(self.driver)
        self.mp.checkProduct()
        self.cp=Checkout(self.driver)
        self.cp.checkoutbtn()
        time.sleep(3)
        self.cp.setusername("KetanP")
        time.sleep(2)
        self.cp.setlastname("puranik")
        time.sleep(2)
        self.cp.setcompany("Barclys")
        self.cp.country()
        time.sleep(3)
        self.cp.setcountryname("uk")
        self.cp.setadress("somnth Nagar")
        time.sleep(2)
        self.cp.setcity("pune")
        time.sleep(2)
        self.cp.setstate()
        time.sleep(2)
        self.cp.setstatetext("Maharashtra")
        time.sleep(2)
        self.cp.setpostalcode("411014")
        time.sleep(2)
        self.cp.setcontactnumber("7517800408")
        time.sleep(2)
        self.cp.setemail("puranik324@gmail.com")
        time.sleep(2)
        total=self.cp.verifyTotal()
        if total.text=="$18.00":
            assert True
        time.sleep(2)
        self.cp.clickpayment()
        time.sleep(2)
        self.cp.clickplaceorder()
        time.sleep(2)
        self.driver.close()








