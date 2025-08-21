class Base():
    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
    def find_element(self,loc):
        return self.driver.find_element(*loc)
    def click(self,loc):
        self.find_element(loc).click()
    def send_keys(self,loc,info):
        self.find_element(loc).send_keys(info)
    def inform(self,loc):
        self.driver.switch_to.frame(self.find_element(loc))
