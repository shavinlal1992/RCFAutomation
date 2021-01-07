from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

class AddAccount():

    botton_accountsTab_xpath="//*[@id='Account_Tab']/a"
    button_accountNew_xpath="//tbody/tr[1]/td[2]/input[1]"

    text_accountName_xpath="//input[@id='j_id0:accSearchForm:j_id3:j_id6:j_id7']"
    picklist_billingCountry_xpath="//th/label[text()='Billing Country']/..//following-sibling::td/div/select"
    picklist_billingState_xpath="//th/label[text()='Billing State']/..//following-sibling::td/span/select"
    text_billingCity_xpath="//th/label[text()='Billing City']/..//following-sibling::td/input"
    text_billingStreet_xpath="//th/label[text()='Billing Street']/..//following-sibling::td/textarea"
    text_billingPostalcode_xpath="//th/label[text()='Billing Postal code']/..//following-sibling::td/input"
    text_telephone_xpath="//th/label[text()='Telephone']/..//following-sibling::td/input"
    text_website_xpath="//th/label[text()='Website']/..//following-sibling::td/input"
    button_searchCreate_xpath="//td[@class='pbButton ']//input[@value='Search/Create Account']"

    gettext_expSectionName_xpath="//h2[contains(text(),'Create New Account')]"

    def __init__(self,driver):
        self.driver=driver

    def clickOnAccountTab(self):
        self.driver.find_element_by_xpath(self.botton_accountsTab_xpath).click()

    def clickOnNewButton(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.button_accountNew_xpath).click()

    def enterAccountName(self,accountName):
        self.driver.find_element_by_xpath(self.text_accountName_xpath).send_keys(accountName)

    def selectBillingCountry(self,billingCountry):
        bCountryList=Select(self.driver.find_element_by_xpath(self.picklist_billingCountry_xpath))
        bCountryList.select_by_visible_text(billingCountry)

    def selectBillingState(self, billingState):
        bStateList = Select(self.driver.find_element_by_xpath(self.picklist_billingState_xpath))
        bStateList.select_by_visible_text(billingState)

    def enterBillingCity(self, billingCity):
        self.driver.find_element_by_xpath(self.text_billingCity_xpath).send_keys(billingCity)

    def enterBillingStreet(self, billingStreet):
         self.driver.find_element_by_xpath(self.text_billingStreet_xpath).send_keys(billingStreet)

    def enterBillingPostacode(self, billingPostalcode):
        self.driver.find_element_by_xpath(self.text_billingPostalcode_xpath).send_keys(billingPostalcode)

    def enterTelephone(self, telephone):
        self.driver.find_element_by_xpath(self.text_telephone_xpath).send_keys(telephone)

    def enterWebsite(self, website):
        self.driver.find_element_by_xpath(self.text_website_xpath).send_keys(website)

    def clickSearchCreateAccount(self):
        self.driver.find_element_by_xpath(self.button_searchCreate_xpath).click()

    def getTheActualSecionName(self):
        return self.driver.find_element_by_xpath(self.gettext_expSectionName_xpath).text
