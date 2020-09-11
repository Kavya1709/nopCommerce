from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_HomePageTitle(self, setup):


        print(self.logger)
        print(self.logger.getEffectiveLevel())
        self.logger.info("*********** Test_001_Login ***********")
        self.logger.info("*********** Verifying homepage title ***********")
        print("test")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_Title = self.driver.title
        if act_Title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("*********** Test case Title is correct ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            assert False
            self.logger.error("*********** Test case Title failed ***********")


    def test_login(self, setup):

        self.logger.info("*********** Verifying login test***********")

        self.driver = setup
        self.driver.get(self.baseURL)

        #Create an object of class Login to access its action methods
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        LoginPageTitle = self.driver.title
        if LoginPageTitle == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Test case Title passed ***********")
            assert True
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.logger.error("*********** Test case Title failed ***********")
            self.driver.close()


