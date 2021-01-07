import pytest
from selenium import webdriver
import configparser

@pytest.yield_fixture()
def setup(browser):

    if browser=='chrome':
        driver=webdriver.Chrome("Drivers\chromedriver.exe")
        print("Launching Chrome Browser.......")
    elif browser=='firefox':
        driver =webdriver.Firefox(executable_path="Drivers\geckodriver.exe")
        print("Launching FireFox Browser.......")
    else:
        driver=webdriver.Ie("Drivers\IEDriverServer.exe")

    yield driver
    driver.close()


def pytest_addoption(parser):   # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()  # This will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


### PyTest HTML Report ###

# It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'RCFAutomation'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Shavin Lal'

# It is a hook for delete/modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)









#@pytest.fixture()
#def setupconfig():
    #config = configparser.ConfigParser()
    #config['DEFAULT'] = {'baseURL': 'https://rubrikinc--rbkqa.my.salesforce.com/','username': 'shavin.lal@rubrik.com.rbkqa', 'password': 'Quali@123'}
    #with open('.//Configurations//config.ini', 'w') as configfile:
        #config.write(configfile)

    #return "Successfully written to the Config.ini file"
