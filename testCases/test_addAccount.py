import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddAccountPage import AddAccount
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
import time

class Test_003_AddAccount:

    baseURL= ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getUserpassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addAccount(self,setup):
        self.logger.info("****** Test_003_AddAccount *******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("****** Login to SF is success *******")
        time.sleep(5)
        self.addacct=AddAccount(self.driver)

        self.addacct.clickOnAccountTab()
        self.addacct.clickOnNewButton()

        self.accountName = random_generatorCharecter()
        self.addacct.enterAccountName(self.accountName)
        self.addacct.selectBillingCountry("India")
        time.sleep(2)
        self.addacct.selectBillingState("Karnataka")
        self.addacct.enterBillingCity("Bangalore")
        self.addacct.enterBillingStreet("Bangalore #1 road")
        self.addacct.enterBillingPostacode("23232")
        self.addacct.enterTelephone("2233223321")
        self.addacct.enterWebsite("www.website.com")
        time.sleep(2)
        self.addacct.clickSearchCreateAccount()
        time.sleep(5)

        self.actualSectionName=self.addacct.getTheActualSecionName()

        if self.actualSectionName == "Create New Account":
            self.logger.info("****Add account test is passed***")
            assert True, self.logger.info(f"expected is Create New Account and got {self.actualSectionName} Matched with expected")
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_addAccount.png")
            self.logger.info("*********** Add account test failed *******")
            assert False, self.logger.info(f"expected was Create New Account but got {self.actualSectionName} Un matched with expected")

        self.logger.info("********Ending Test_003_AddAccount****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for  x in range(size))

def random_generatorCharecter(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for  x in range(size))
