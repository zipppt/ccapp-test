import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared1 import doForm
from shared import doLogin

class CCAPPVIP_Shining_Star_Award(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()

    def doLogin(self):
        doLogin(self.driver)

    def doForm(self):
        doForm(self.driver)

    def test_ccapp_Shining_Star_Award (self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcome", driver.title)

        self.doLogin()

        element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[7]/a")
        element.click()

        self.doForm()


        element = driver.find_element_by_xpath("//div[@class='form_block']/a[@id='submit_button']/span")
        element.click()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


