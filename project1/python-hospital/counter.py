# -*- coding: utf-8 -*-
"""
Created on Tue May 19 00:43:02 2020

@author: che
"""

from flask import Flask
from firebase import firebase
import time
import urllib.request as request

p_url = 'https://fingerprint-chara.firebaseio.com/'
fdb = firebase.FirebaseApplication(p_url,None)

hos101 = fdb.get('/骨科101病房',None)
hos102 = fdb.get('/骨科102病房',None)
hos201 = fdb.get('/骨科201病房',None)
hos202 = fdb.get('/病人基本資料全/張喬喆P124379775',None)
hoshis = fdb.get('/病人基本資料全',None)

counter=Flask(__name__)                                                                             #_name_代表目前執行的模組

@counter.route("/")
def home():                                                                                     # 涵式的裝飾 (Decorator): 已函式為基礎，提供附加的功能
    return"this is hospital."

@counter.route("/hospital101")                                                                      #代表要處理的網站路徑
def test101():                                                                                  #房號及床號101
    return str(hos101)

@counter.route("/hospital102")                                                                      #代表要處理的網站路徑
def test102():                                                                                  #房號及床號102
    return str(hos102)

@counter.route("/hospital201")                                                                      #代表要處理的網站路徑
def test201():                                                                                  #房號及床號201
    return str(hos201)

@counter.route("/hospital202")                                                                      #代表要處理的網站路徑
def test202():                                                                                  #房號及床號202
    return str(hos202)

@counter.route("/hospitalhis")                                                                      #代表要處理的網站路徑
def testhis():                                                                                  #歷史病例
    return str(hoshis)

if __name__=="__main__":                                                                          #如果以主程式執行
        counter.run()                                                                                     