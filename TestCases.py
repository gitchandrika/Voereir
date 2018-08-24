'''
Created on Aug 24, 2018

@author: Chandrika Bhartiiya
'''

from selenium import webdriver
import unittest
import PageObject

class test_cases(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://voereir.com/index.html")

    def tearDown(self):
        driver.quit()
        
    def test_switching_tabs(self):
        print "Browser Opened for Test case1- Perform Switching between tabs"
        obj = PageObject.PageVoereir()
        tabs_list = {'Home', 'About', 'Product', 'Services', 'Contact', 'Careers', 'Login',}
        for tab in tabs_list:
            obj.click_on_tabs(driver, tab)
  
    def test_try_login(self):
        obj = PageObject.PageVoereir()
        obj.click_on_tabs(driver, tab_name = 'Careers')
        driver.find_element_by_xpath("(//div[@class='row in-line']//a)[1]").click()
        driver.switch_to_window(driver.window_handles[0])

    def test_login(self):
        obj = PageObject.PageVoereir()
        login_msg = obj.click_on_tabs(driver, tab_name = 'Login')\
                        .input_data(driver, 'User', 'Some_userName')\
                        .input_data(driver, 'Password', 'SomePassword')\
                        .click_Login(driver)
        assert login_msg == 'Authentication failed'
        
 
if __name__ == '__main__':
    unittest.main()