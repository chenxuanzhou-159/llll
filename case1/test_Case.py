import pytest
from selenium import webdriver
from case1.Page import Page

class TestCase():
    def test_01(self,driver):
        f=Page(driver)
        f.test_luoji()



