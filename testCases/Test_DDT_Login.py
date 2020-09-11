from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login ***********")
        self.logger.info("*********** Verifying login DDT test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
       #self.driver.maximize_window()

        self.lp = Login(self.driver)       # Create an object of class Login to access its action methods

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No. of rows:", self.rows)

        list_status = []
        # Read the data from excel
        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("******** Passed *********")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("********* Failed *********")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("********* Failed ***********")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("********** Passed **********")
                    list_status.append("Pass")
            print(list_status)

        if "Fail" not in list_status:
            self.logger.info("********** Login DDT test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT test Failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT test ********")
        self.logger.info("******* Completed Test_002_DDT_Login **********")


