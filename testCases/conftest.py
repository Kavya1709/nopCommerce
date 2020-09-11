from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r'C:\Users\Kavya Jeevan\PycharmProjects\nopcommerceApp\venv\Lib\site-packages\selenium\webdriver\common\chromedriver.exe')
        print("*********** Launching Chrome browser ************")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'C:\Users\Kavya Jeevan\PycharmProjects\nopcommerceApp\venv\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
        print("*********** Launching Firefox browser ************")
    return driver


def pytest_addoption(parser):            # This will get the value from the CLI/ Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                   # This will return the browser value to setup method
    return request.config.getoption("--browser")



################# PyTest HTML Reports ################

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Kavya'

# Hook for delete/modify info to HTML Report
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

