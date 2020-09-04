from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Checkout:
    btn_checkout_xpath="//button[@class='ui purple fluid button']"
    text_box_name="billing_first_name"
    text_lastname_id="billing_last_name"
    text_company_id="billing_company"
    select_country_id="select2-billing_country-container"
    select_text_xpath="//input[@class='select2-search__field"
    text_address_id="billing_address_1"
    text_city_id="billing_city"
    select_state_xpath="//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//span[@class='select2-selection select2-selection--single']"
    select_statetext_xpath="//input[@class='select2-search__field']"
    text_zip_id="billing_postcode"
    text_phone_id="billing_phone"
    text_email_id="billing_email"
    verify_price_xpath="//tr[@class='order-total']//span[@class='woocommerce-Price-amount amount'][contains(text(),'18.00')]"
    btn_id="payment_method_paypal"
    btn_placeorder_id="place_order"

    def __init__(self,driver):
        self.driver=driver

    def checkoutbtn(self):
        self.driver.find_element_by_id(self.btn_checkout_xpath).click()

    def setusername(self,username):
        self.driver.find_element_by_name(self.text_box_name).send.keys(username,Keys.TAB)

    def setlastname(self,lastname):
        self.driver.find_element_by_id(self.text_lastname_id).send_keys(lastname,Keys.TAB)
    
    def setcompany(self,cpmname):
        self.driver.find_element_by_id(self.text_company_id).send.Keys(cpmname,Keys.TAB)

    def country(self):
        self.driver.find_element_by_id(self.select_country_id).click()

    def setcountryname(self,countryname):
        self.driver.find_element_by_xpath(self.select_text_xpath).send_keys(countryname,Keys.ENTER)

    def setadress(self,adress):
        self.driver.find_element_by_id(self.text_address_id).send_keys(adress,Keys.TAB)

    def setcity(self,city):
        self.driver.find_element_by_id(self.text_city_id).send_keys(city,Keys.TAB)

    def setstate(self):
        self.driver.find_element_by_xpath(self.select_state_xpath).click()

    def setstatetext(self,statename):
        self.driver.find_element_by_xpath(self.select_statetext_xpath).send_keys(statename,Keys.ENTER)

    def setpostalcode(self,zip):
        self.driver.find_element_by_id(self.text_zip_id).send_keys(zip,Keys.TAB)

    def setcontactnumber(self,ctnum):
        self.driver.find_element_by_id(self.text_phone_id).send_keys(ctnum.Keys.TAB)


    def setemail(self,email):
        self.driver.find_element_by_id(self.text_email_id).send_keys(email,Keys.TAB)

    def verifyTotal(self):
        self.driver.find_element_by_xpath(self.verify_price_xpath)

    def clickpayment(self):
        self.driver.find_element_by_id(self.btn_id).click()

    def clickplaceorder(self):
        self.driver.find_element_by_id(self.btn_placeorder_id).click()

