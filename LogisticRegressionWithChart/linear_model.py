#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import numpy
import json
from sklearn import linear_model as lm
import pymysql.cursors

# read training data
data = pandas.read_csv("training.csv")
pdX = data["value"]
npX = numpy.array(pdX)
npX = npX.reshape(-1, 1)

pdY = data["status"]
npY = numpy.array(pdY)

# sklearn
clf = lm.LogisticRegression()
clf.fit(npX, npY)

# test status
# status = clf.predict(499)

# connect db
db = pymysql.connect("172.32.19.7", "iot", "iot", "lightdb")
cursor = db.cursor()

# 執行SQL語法查詢
cursor.execute("SELECT value, status FROM light")

# 把搜尋出來的解果轉為ndarray
rowValue = [item[0] for item in cursor.fetchall()]
predictValues = numpy.array(rowValue)
predictValues = predictValues.reshape(-1, 1)

# 把values丟到LogisticRegression預測狀態
predictStatus = clf.predict(predictValues)

# 關閉資料庫
db.close()

# 輸出結果
status = predictStatus.tolist()
result = json.dumps([{'value': rowValue, 'status': status} for rowValue, status in zip(rowValue, status)])
print(result)