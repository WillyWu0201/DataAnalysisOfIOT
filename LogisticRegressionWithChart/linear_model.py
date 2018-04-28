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
cursor.execute("SELECT * FROM light")

# 整理搜尋出來的資料
id_list = []
value_list = []
results = cursor.fetchall()
for row in results:
  id_list.append(row[0])
  value_list.append(row[1])

# 把結果轉為ndarray
predictValues = numpy.array(value_list)
predictValues = predictValues.reshape(-1, 1)

# 把values丟到LogisticRegression預測狀態
predictStatus = clf.predict(predictValues)
status_list = predictStatus.tolist()

# 更新資料庫狀態
for i in range(len(id_list)):
  id = id_list[i]
  status = status_list[i]
  cursor.execute("update light set status = %d where id = %d" % (status, id))
  db.commit()

# 關閉資料庫
db.close()

# 輸出結果
result = json.dumps([{'value': rowValue, 'status': status} for rowValue, status in zip(value_list, status_list)])
print(result)