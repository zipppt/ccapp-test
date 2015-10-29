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
        Visionary = driver.find_element_by_css_selector('a.btn.btn-primary.log-in')
        Visionary.click()
        username = driver.find_element_by_id('id_username')
        username.send_keys("zipppt@gmail.com")
        password = driver.find_element_by_id('id_password')
        password.send_keys("zipppt2016")
        log = driver.find_element_by_id('submit_button')
        log.click()
        Visionary = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[3]/a")
        Visionary.click()
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_nominator_name']/input")
        Visionary.clear()
        Visionary.send_keys("Andrew Trofimchuk")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_nominator_email']/input")
        Visionary.clear()
        Visionary.send_keys("zipppt@gmail.com")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_nominator_phone']/input")
        Visionary.clear()
        Visionary.send_keys("222-222-2222")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_name']/input")
        Visionary.clear()
        Visionary.send_keys("Andrew")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_address']/input")
        Visionary.clear()
        Visionary.send_keys("Golosiivska St.")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_city']/input")
        Visionary.clear()
        Visionary.send_keys("Sacramento")
        element = self.driver.find_element_by_id('id_state')
        select = Select(element)
        select.select_by_visible_text("California")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_zip']/input")
        Visionary.clear()
        Visionary.send_keys("11111")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_home_phone']/input")
        Visionary.clear()
        Visionary.send_keys("222-222-2222")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_work_phone']/input")
        Visionary.clear()
        Visionary.send_keys("333-333-3333")
        Visionary = driver.find_element_by_xpath("//div[@id='div_id_bio']/textarea")
        Visionary.clear()
        Visionary.send_keys("aaaaaaaaaaa")
        Visionary = driver.find_element_by_xpath("//div[@class='form_block']/a[@id='submit_button']/span")
        Visionary.click()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()

