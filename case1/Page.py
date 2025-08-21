import time

from selenium.webdriver.common.by import By

from case1.Base import Base

class Page(Base):
    xpath_inform=By.XPATH,'/html/body/div[3]/div[3]/div[1]/div/div[3]/div[1]/div[2]/iframe'
    name_email=By.NAME,"email"
    name_password=By.NAME,'password'
    id_login=By.ID,'dologin'
    def inform_url(self):
        self.inform(self.xpath_inform)
    def email(self):
        self.send_keys(self.name_email,"17634416495")
    def password(self):
        self.send_keys(self.name_password,"123456Aa")
    def login(self):
        self.click(self.id_login)
    def test_luoji(self):
        self.open_url("https://mail.163.com/")
        self.inform_url()
        self.email()
        self.password()
        time.sleep(2)
        self.login()
        time.sleep(3)
