

from selenium import webdriver

class infow():

    def _init_(self):
         self.driver = webdriver.Chrome(executable_path='c;/users/dell/.wdm/drivers/chromedrive/win32/85.0.4183.87/chromedriver.exe')
    def get_infow(self, query):
        self.query = query
        self.driver.get(url="http://www.wikipedia.org/")
        search=self.driver.find_element_by_xpath('//*[@id="search-input"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button]')
        enter.click()

        assist=infow()
        assist.get_infow("neutron stars")