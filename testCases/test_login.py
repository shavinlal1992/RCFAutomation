import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL= ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getUserpassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        
        self.logger.info("************* Test_001_Login *******")
        self.logger.info("************* Verifying Home Page Title *******")
        # Utilizing the setup Fixtures to avoid the driver initialization redundancy over each test cases
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title

        if actual_title=="Login | Salesforce":
            assert True
            self.logger.info("************* Home Page Title Test Is Passed *******")

        else:
            self.driver.save_screeshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("************* Home Page Title Test Is Failed *******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("************* Verifying Login Test *******")
        #Utilizing the setup Fixtures to avoid the driver initialization redundancy over each test cases
        self.driver=setup
        self.driver.get(self.baseURL)

        #Create Object of LoginPage Class in order to call the functions
        self.lp=LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title=self.driver.title
        self.logger.info(actual_title)

        if actual_title=="Salesforce - Unlimited Edition":
            assert True
            self.logger.info("************* Login Test Is Passed *******")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************* Login Test Is Failed *******")
            assert False




