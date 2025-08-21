import json
from dotenv import load_dotenv
import pytest
import requests
import os

from selenium import webdriver
load_dotenv()

@pytest.fixture(scope="session")
def handers_url():
    hander=login_url()
    handersl={
        "userId":str(hander[0]),
        "sessionId":str(hander[1])
    }
    # print(handersl)
    return handersl


def login_url():
    url=os.getenv("url")+os.getenv("login")
    body={
        "email":"1478997572@qq.com",
        "pwd":"eWLPHopE945d2ivttHaQTQ=="
    }
    r=requests.post(url,data=body).json()
    print("登录成功",json.dumps(r,indent=4,ensure_ascii=False))
    return r["result"]["userId"],r["result"]["sessionId"]

@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
