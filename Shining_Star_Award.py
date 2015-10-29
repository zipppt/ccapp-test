import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcom", driver.title)
        #ниже две строки для разлогина
        #RADTII = driver.find_element_by_xpath("//div[@id='main-nav']/div[@id='tools-nav']/ul[1]/li[5]/a")
        #RADTII.click()
        Shining = driver.find_element_by_css_selector('a.btn.btn-primary.log-in')
        Shining.click()
        username = driver.find_element_by_id('id_username')
        username.send_keys("zipppt@gmail.com")
        password = driver.find_element_by_id('id_password')
        password.send_keys("zipppt2016")
        log = driver.find_element_by_id('submit_button')
        log.click()
        Shining = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[7]/a")
        Shining.click()
        Shining = driver.find_element_by_xpath("//div[@id='div_id_nominator_name']/input")
        Shining.clear()
        Shining.send_keys("Andrew Trofimchuk")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_nominator_email']/input")
        Shining.clear()
        Shining.send_keys("zipppt@gmail.com")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_nominator_phone']/input")
        Shining.clear()
        Shining.send_keys("222-222-2222")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_name']/input")
        Shining.clear()
        Shining.send_keys("Andrew")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_address']/input")
        Shining.clear()
        Shining.send_keys("Golosiivska St.")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_city']/input")
        Shining.clear()
        Shining.send_keys("Sacramento")
        element = self.driver.find_element_by_id('id_state')
        select = Select(element)
        select.select_by_visible_text("California")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_zip']/input")
        Shining.clear()
        Shining.send_keys("11111")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_home_phone']/input")
        Shining.clear()
        Shining.send_keys("222-222-2222")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_work_phone']/input")
        Shining.clear()
        Shining.send_keys("333-333-3333")
        Shining = driver.find_element_by_xpath("//div[@id='div_id_bio']/textarea")
        Shining.clear()
        Shining.send_keys("aaaaaaaaaaa")
        Shining = driver.find_element_by_xpath("//div[@class='form_block']/a[@id='submit_button']/span")
        Shining.click()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


