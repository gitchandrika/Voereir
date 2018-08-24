'''
Created on Aug 24, 2018

@author: Chandrika Bhartiiya
'''


class PageVoereir:

 
    def click_on_tabs(self, driver, tab_name):
        """
        This method will click on the tabs present on the page.
        """
        print "Clicking On tab {}".format(tab_name)
        driver.find_element_by_xpath("//a[contains(@class,'page-scroll')][text()='{}']".format(tab_name))\
                .click()
        return self

    def input_data(self, driver, enter_in, to_enter):
        print "Entering {} in {}.".format(to_enter, enter_in)
        enter_text_in = driver.find_element_by_xpath("//input[@placeholder='{}']".format(enter_in))
        enter_text_in.send_keys(to_enter)
        return self
    
    def click_Login(self, driver):
        driver.find_element_by_xpath("//a[@class='btn btn-primary custom-button'][text()='Login']").click()
        loginmsg = driver.find_element_by_id("loginmsg").text
        return loginmsg
                
    
        