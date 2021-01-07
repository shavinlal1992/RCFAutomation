import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:

    baseURL= ReadConfig.getApplicationURL()
    path=".//TestData//LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("************* Test_002_DDT_Login Started *******")
        self.logger.info("************* Verifying test_login_ddt Test Case *******")

        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        self.logger.info("The row counts is %s",self.rows)

        list_status=[]  # Empty list variable

        for r in range (2,self.rows+1):

            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.logger.info('username is %s',self.username)
            self.logger.info('password is %s',self.password)
            self.logger.info('expected result is %s',self.exp)

            time.sleep(5)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title=self.driver.title
            exp_title="Salesforce - Unlimited Edition"

            if actual_title==exp_title:
                self.logger.info("************* Login Is successful due to Correct credentials *******")
                if self.exp=="Pass":
                    self.logger.info("*******Test Data sheet expected given as Pass So the test also passed *******")
                    self.lp.clickLogout()
                    list_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("************* Test Data sheet expected given as Fail rather than Pass *******")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif actual_title != exp_title:
                self.logger.info("************* Login Failed due to incorrect credentials *******")
                if self.exp=="Pass":
                    self.logger.info("************* Test Data sheet expected given as Pass rather than Fail *******")
                    list_status.append("Fail")

                elif self.exp=="Fail":
                    self.logger.info("****** Test Data sheet expected given as Fail So the test also passed *******")
                    list_status.append("Pass")

        self.logger.info("The status in the list are: ")
        for item in list_status:
            self.logger.info(item)

        if "Fail" not in list_status:
            self.logger.info("*** Login DDT test is passed ***")
            assert True
        else:
            self.logger.info("*** Login DDT test is Failed ***")
            assert False

        self.logger.info("*** End of Verifying test_login_ddt ***")
        self.logger.info("*** Completed Test_002_DDT_Login ***")