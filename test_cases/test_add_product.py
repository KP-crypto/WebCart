import time
from selenium import webdriver
import pytest
from pages.websitePages import mainPage
from Utilities.customlogger import LogGen
from Utilities.readProperties import Readconfig


class Test_001:
    url=Readconfig.getApplicationURL()
    logger=LogGen.loggen()


    @pytest.mark.sanity
    def test_homepageTitle(self,setup):
        self.logger.info("############ Home Page Test Strted#########")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()


        title=self.driver.title
        if title=="pwa-theme-woocommerce":
            self.logger.info("######## Title Test Passed##########")
            assert True
            self.driver.close()


    @pytest.mark.regression
    def test_addProduct(self,setup):
        self.logger.info("########## Product Test Started")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.mp=mainPage(self.driver)
        self.mp.checkProduct()
        self.message=self.mp.verifyProduct()
        print(self.message.text)
        assert "Happy Ninja" in self.message.text
        time.sleep(3)
        self.driver.close()








