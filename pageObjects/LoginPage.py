from selenium import webdriver

class LoginPage:

    text_username_id="username"
    text_password_id="password"
    button_login_xpath="//input[@id='Login']"
    button_logoutarrow_id="userNav-arrow"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logoutarrow_id).click()
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()