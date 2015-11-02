from selenium.webdriver.support.ui import Select


def doOpen(driver):
    driver.get("http://ccapp-test.marpasoft.com/")


def doLogin(driver):
    element = driver.find_element_by_css_selector('a.btn.btn-primary.log-in')
    element.click()
    username = driver.find_element_by_id('id_username')
    username.send_keys("zipppt@gmail.com")
    password = driver.find_element_by_id('id_password')
    password.send_keys("zipppt2016")
    log = driver.find_element_by_id('submit_button')
    log.click()


def doForm(driver):
    element = driver.find_element_by_xpath("//div[@id='div_id_nominator_name']/input")
    element.clear()
    element.send_keys("Andrew Trofimchuk")
    element = driver.find_element_by_xpath("//div[@id='div_id_nominator_email']/input")
    element.clear()
    element.send_keys("zipppt@gmail.com")
    element = driver.find_element_by_xpath("//div[@id='div_id_nominator_phone']/input")
    element.clear()
    element.send_keys("222-222-2222")
    element = driver.find_element_by_xpath("//div[@id='div_id_name']/input")
    element.clear()
    element.send_keys("Andrew")
    element = driver.find_element_by_xpath("//div[@id='div_id_address']/input")
    element.clear()
    element.send_keys("Golosiivska St.")
    element = driver.find_element_by_xpath("//div[@id='div_id_city']/input")
    element.clear()
    element.send_keys("Sacramento")
    element = driver.find_element_by_id('id_state')
    select = Select(element)
    select.select_by_visible_text("California")
    element = driver.find_element_by_xpath("//div[@id='div_id_zip']/input")
    element.clear()
    element.send_keys("11111")
    element = driver.find_element_by_xpath("//div[@id='div_id_home_phone']/input")
    element.clear()
    element.send_keys("222-222-2222")
    element = driver.find_element_by_xpath("//div[@id='div_id_work_phone']/input")
    element.clear()
    element.send_keys("333-333-3333")
    element = driver.find_element_by_xpath("//div[@id='div_id_bio']/textarea")
    element.clear()
    element.send_keys("aaaaaaaaaaa")


def doPersonaInformation(driver):
    element = driver.find_element_by_xpath("//div[@class='wrapit']/h4[1]/a")
    element.click()
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-first_name']/input")
    element.clear()
    element.send_keys("Andrew")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-last_name']/input")
    element.clear()
    element.send_keys("Trofimchuk")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-middle_name']/input")
    element.clear()
    element.send_keys("Nikola")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_month')
    select = Select(element)
    select.select_by_visible_text("July")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_day')
    select = Select(element)
    select.select_by_visible_text("6")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_year')
    select = Select(element)
    select.select_by_visible_text("1978")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-ssn']/input")
    element.clear()
    element.send_keys("2222")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-street']/input")
    element.clear()
    element.send_keys("Golosiivska St.")
    element = driver.find_element_by_id('id_personal_info-state')
    select = Select(element)
    select.select_by_visible_text("California")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-city']/input")
    element.clear()
    element.send_keys("Sacramento")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-zip']/input")
    element.clear()
    element.send_keys("11111")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-phone']/input")
    element.clear()
    element.send_keys("111-111-1111")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-email']/input")
    element.clear()
    element.send_keys("zipppt@gmail.com")
    element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
    element.click()


def doApply(driver):
    element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()


def doSubmit(driver):
    element = driver.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
    element = driver.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()


def doClean(driver):
    driver.get("http://ccapp-test.marpasoft.com/admin/profiles/profile/148208/")
    element = driver.find_element_by_xpath("//input[@id='id_application_set-0-DELETE']")
    element.click()
    element = driver.find_element_by_xpath("//input[@class='default']")
    element.click()


def doVisionary_Award(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[3]/a")
    element.click()


def doAbove(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[4]/a")
    element.click()


def doShining_Star_Award(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[7]/a")
    element.click()


def doSpotlight_Award(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[6]/a")
    element.click()


def doVIP_Award(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[5]/a")
    element.click()


def doForm2(driver):
    element = driver.find_element_by_xpath("//div[@id='div_id_course_name']/input")
    element.send_keys("Course name")
    element = driver.find_element_by_xpath("//div[@id='div_id_course_id']/input")
    element.send_keys("Course id")
    element = driver.find_element_by_xpath("//div[@id='div_id_school_name']/input")
    element.send_keys("School name")
    element = driver.find_element_by_id('id_academic_content_area')
    select = Select(element)
    select.select_by_visible_text("Physiology and Pharmacology")
    element = driver.find_element_by_xpath("//div[@id='div_id_hours']/input")
    element.clear()
    element.send_keys('45')
    element = driver.find_element_by_id('id_grade')
    select = Select(element)
    select.select_by_visible_text("A")
    element = driver.find_element_by_xpath("//div[@id='div_id_completion_date']/input")
    element.send_keys("11/20/14")
    element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
    element.click()


def doRadt2(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[3]/a")
    element.click()


def doRadt1(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[2]/a")
    element.click()


def doRegHis(driver):
    element = driver.find_element_by_xpath("//div[@id='div_id_registered']/input")
    element.click()
    element = driver.find_element_by_id('id_initial_date_month')
    select = Select(element)
    select.select_by_visible_text("July")
    element = driver.find_element_by_id('id_initial_date_day')
    select = Select(element)
    select.select_by_visible_text("6")
    element = driver.find_element_by_id('id_initial_date_year')
    select = Select(element)
    select.select_by_visible_text("2015")
    element = driver.find_element_by_xpath("//input[@id='id_current_organization_0']")
    element.click()
    element = driver.find_element_by_xpath("//input[@id='id_certified']")
    element.click()
    element = driver.find_element_by_xpath("//input[@id='id_have_ever_revoked_0']")
    element.click()


def doCadc1(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[5]/a")
    element.click()


def doTraditional_Method(driver):
    element = driver.find_element_by_xpath("//input[@id='id_education_method_0']")
    element.click()


def doCCAPP2(driver):
    element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][1]/ul[3]/li[2]/a")
    element.click()
    element = driver.find_element_by_xpath("//div[@class='b-str blog-post']/h4[1]/a")
    element.click()

    element = driver.find_element_by_id('id_registration_type')
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
    element.send_keys("Certificate number  5")
    element = driver.find_element_by_xpath("//div[@id='div_id_street']/input")
    element.clear()
    element.send_keys("Golosiivska St.")
    element = driver.find_element_by_xpath("//div[@id='div_id_city']/input")
    element.clear()
    element.send_keys("Sacramento")
    element = driver.find_element_by_id('id_state')
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
    element.send_keys("zipppt@gmail.com")
    element = driver.find_element_by_xpath("//div[@id='div_id_ccapp_board_member']/input")
    element.click()
    element = driver.find_element_by_xpath("//div[@id='div_id_speaker_presenter']/input")
    element.click()
    element = driver.find_element_by_xpath(
        "//div[@id='div_id_special_access_needs']/textarea[@id='id_special_access_needs']")
    element.clear()
    element.send_keys("Full access")
    element = driver.find_element_by_xpath("//div[@id='div_id_special_dietary_needs']/input")
    element.clear()
    element.send_keys("Vegan, але їм сало)")
    element = driver.find_element_by_xpath("//div[@id='div_id_period_full']/input")
    element.click()
    #element = driver.find_element_by_xpath("//div[@id='div_id_period_thursday']/input")
    #element.click()
    #element = driver.find_element_by_xpath("//div[@id='div_id_period_friday']/input")
    #element.click()
    #element = driver.find_element_by_xpath("//div[@id='div_id_period_saturday']/input")
    #element.click()
    #element = driver.find_element_by_xpath("//div[@id='div_id_period_sunday']/input")
    #element.click()
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
