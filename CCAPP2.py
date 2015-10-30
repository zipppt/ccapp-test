import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin



class CCAPPCCAPP2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def doLogin(self):
        doLogin(self.driver)

    def test_ccapp_CCAPP2(self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcom", driver.title)
        self.doLogin()

        element= driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[2]/a")
        element.click()
        element = driver.find_element_by_xpath("//div[@class='b-str blog-post']/h4[1]/a")
        element.click()
        element = self.driver.find_element_by_id('id_registration_type')
        select = Select(element)
        select.select_by_visible_text("Student")
        element = driver.find_element_by_xpath("//div[@id='div_id_first_name']/input")
        element.clear()
        element.send_keys("Andrew")
        element = driver.find_element_by_xpath("//div[@id='div_id_last_name']/input")
        element.clear()
        element.send_keys("Trofimchuk")
        element = driver.find_element_by_xpath("//div[@id='div_id_middle_name']/input")
        element.clear()
        element.send_keys("Nikola")
        element = driver.find_element_by_xpath("//div[@id='div_id_badge_name']/input")
        element.clear()
        element.send_keys("Andruan")
        element = driver.find_element_by_xpath("//div[@id='div_id_certifications']/textarea[@id='id_certifications']")
        element.clear()
        element.send_keys("Certificat namber 5")
        element = driver.find_element_by_xpath("//div[@id='div_id_street']/input")
        element.clear()
        element.send_keys("Golosiivska St.")
        element = driver.find_element_by_xpath("//div[@id='div_id_city']/input")
        element.clear()
        element.send_keys("Sacramento")
        element = self.driver.find_element_by_id('id_state')
        select = Select(element)
        select.select_by_visible_text("California")
        element = driver.find_element_by_xpath("//div[@id='div_id_zip']/input")
        element.clear()
        element.send_keys("11111")
        element = driver.find_element_by_xpath("//div[@id='div_id_phone']/input")
        element.clear()
        element.send_keys("111-111-1111")
        element = driver.find_element_by_xpath("//div[@id='div_id_fax']/input")
        element.clear()
        element.send_keys("222-222-2222")
        element = driver.find_element_by_xpath("//div[@id='div_id_email']/input")
        element.clear()
        element.send_keys("zipppt@gmail.com")
        element = driver.find_element_by_xpath("//div[@id='div_id_employer']/input")
        element.clear()
        element.send_keys("ziptt@mail.ru")
        element = driver.find_element_by_xpath("//div[@id='div_id_ccapp_board_member']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_speaker_presenter']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_special_access_needs']/textarea[@id='id_special_access_needs']")
        element.clear()
        element.send_keys("Full access")
        element = driver.find_element_by_xpath("//div[@id='div_id_special_dietary_needs']/input")
        element.clear()
        element.send_keys("Vegan, але їм сало)")
        element = driver.find_element_by_xpath("//div[@id='div_id_period_full']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_period_thursday']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_period_friday']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_period_saturday']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_period_sunday']/input")
        element.click()
        # тут исчезло название программы которую типа хош пройти, так как уже оплатил бля
        #element = driver.find_element_by_xpath("//div[@id='div_id_member_program']/input")
        #element.clear()
        #element.send_keys("название программы")
        element = driver.find_element_by_xpath("//div[@id='div_id_extra_meals_lunch']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_extra_meals_dinner']/input")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_raffle_tickets']/input")
        element.clear()
        element.send_keys("2")
        element = driver.find_element_by_xpath("//div[@id='div_id_mugs']/input")
        element.clear()
        element.send_keys("1")

        #element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
        #element.click()
        #element = driver.find_element_by_xpath("//div[@class='form_block']/a[@class='btn btn-primary']/span")
        #element.click()





    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


