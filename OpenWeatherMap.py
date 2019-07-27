#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import datetime
import os
import requests
import sys

from pytz import timezone

API_URL = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'

class OpenWeatherMap :
    # 初期処理
    def __init__(self,API_KEY,ZIP) :
        self.API_KEY = API_KEY
        self.ZIP = ZIP
        self.update()
        print("start")

    def update(self):
        url = API_URL.format(self.ZIP, self.API_KEY)
        response = requests.get(url)
        self.forecastData = json.loads(response.text)

        if not ('list' in self.forecastData):
            print('error')
            return
            
    def get(self):
        dt_now = datetime.datetime.now() # + datetime.timedelta(days=1) 最終的にはtimedeltaを消す
        for item in self.forecastData['list']:
            forecastDatetime = timezone('Asia/Tokyo').localize(datetime.datetime.fromtimestamp(item['dt']))
            weatherDescription = item['weather'][0]['description']
            if dt_now.year == forecastDatetime.year and dt_now.month == forecastDatetime.month and dt_now.day == forecastDatetime.day :
                if '雨' in weatherDescription :
                    return True
        return False
