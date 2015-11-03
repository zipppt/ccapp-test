import unittest
from selenium import webdriver
from shared import doLogin, doPersonaInformation1, doSubmit, doClean, doApply, doOpen, doForm3, doLAADC



class CCAPPLAADC2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)
    def doLogin(self):
        doLogin(self.driver)
    def doLAADC(self):
        doLAADC(self.driver)
    def doPersonaInformation1(self):
        doPersonaInformation1(self.driver)
    def doSubmit(self):
        doSubmit(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doForm3(self):
        doForm3(self.driver)
    def doClean(self):
        doClean(self.driver)

    def test_ccapp_LAADC2(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doLAADC()
        self.doPersonaInformation1()
        self.doSubmit()

# тут приаттачить документ
        self.doClean()


    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


