import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin, doOpen, doCCAPP2, doApply



class CCAPPCCAPP2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)

    def doLogin(self):
        doLogin(self.driver)
    def doCCAPP2(self):
        doCCAPP2(self.driver)
    def doApply(self):
        doApply(self.driver)

    def test_ccapp_CCAPP2(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doCCAPP2()
        self.doApply()



        #element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
        #element.click()
        #element = driver.find_element_by_xpath("//div[@class='form_block']/a[@class='btn btn-primary']/span")
        #element.click()





    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


