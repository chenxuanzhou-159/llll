import json
import logging
import os

import pytest
import requests

from utils.md5gp import md5_zc

from dotenv import load_dotenv
load_dotenv()


class TestXDGP():
    movieid=None
    cinemaid=None
    scheduleId=None
    @pytest.mark.test()
    def test_01(self,handers_url):
        url = os.getenv("url") + os.getenv("findHotMovieList")
        body = {
            "page":1,
            "count":10
        }
        r=requests.get(url,headers=handers_url,params=body).json()
        print("查询热门电影列表", json.dumps(r, indent=4, ensure_ascii=False))
        TestXDGP.movieid=r["result"][5]["movieId"]
        print(TestXDGP.movieid)

    @pytest.mark.test()
    def test_02(self,handers_url):
        url = os.getenv("url") + os.getenv("findRecommendCinemas")
        body = {
            "page":1,
            "count":10
        }
        r=requests.get(url,headers=handers_url,params=body).json()
        print("查询推荐影院信息", json.dumps(r, indent=4, ensure_ascii=False))
        TestXDGP.cinemaid=r["result"][5]["id"]
        print(TestXDGP.cinemaid)

    @pytest.mark.test()
    def test_03(self, handers_url):
        url = os.getenv("url") + os.getenv("findMovieSchedule")
        body = {
            "movieId": TestXDGP.movieid,
            "cinemaId": TestXDGP.cinemaid
        }
        r = requests.get(url, headers=handers_url,params=body).json()
        print("根据电影ID和影院ID查询电影排期列表", json.dumps(r, indent=4, ensure_ascii=False))
        logging.info("根据电影ID和影院ID查询电影排期列表")
        TestXDGP.scheduleId = r["result"][0]["id"]
        print(TestXDGP.scheduleId)

    def test_04(self,handers_url):
        url = os.getenv("url") + os.getenv("buyMovieTickets")
        c=handers_url.get("userId")+str(TestXDGP.scheduleId)+"movie"
        body = {
            "scheduleId":TestXDGP.scheduleId,
            "seat":["3-7"],
            "sign":md5_zc(c)
        }
        r=requests.post(url,headers=handers_url,json=body).json()
        print("查询推荐影院信息", json.dumps(r, indent=4, ensure_ascii=False))
        logging.info("查询推荐影院信息")


