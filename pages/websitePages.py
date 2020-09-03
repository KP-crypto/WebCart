from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mainPage:
    btn_click_xpath= "//body//div[@class='pusher']//div//div[2]//div[2]//a[1]//button[1]"
    click_btn_addcart_xpath = "//button[@class='ui purple fluid button']"
    cart_click_xpath = "//i[@class='cart large icon shop-icon']"
    text_xpath = "//div[@class='four wide column break-words']"


    def __init__(self,driver):
        self.driver=driver

    def checkProduct(self):
        self.driver.find_element_by_xpath(self.btn_click_xpath).click()

        self.wait=WebDriverWait(self.driver,10)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.click_btn_addcart_xpath))).click()

        self.driver.find_element_by_xpath(self.cart_click_xpath).click()

    def verifyProduct(self):
        message=self.driver.find_element_by_xpath(self.text_xpath)
        return message












