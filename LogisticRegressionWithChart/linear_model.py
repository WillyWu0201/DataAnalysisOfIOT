#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import pandas
import numpy
import json
from sklearn import linear_model as lm

# read training data
data = pandas.read_csv("training.csv")
pdX = data["value"]
npX = numpy.array(pdX)
npX = npX.reshape(-1, 1)

pdY = data["status"]
npY = numpy.array(pdY)

# read testing data
test = pandas.read_csv("testing.csv")
t_pdX = test["value"]
t_npX = numpy.array(t_pdX)
t_npX = t_npX.reshape(-1, 1)

# sklearn
clf = lm.LogisticRegression()
clf.fit(npX, npY)

# test status
status = clf.predict(499)

# predict testing data
t_npY = clf.predict(t_npX)
dict1 = {
        "value": t_pdX,
        "status": t_npY
        }

dataOut = pandas.DataFrame(dict1, columns = ["value", "status"])

# write to csv
# dataOut.to_csv("result.csv")
data = {'value': 500}

json = json.dumps(dataOut)
print(json)
# print(dataOut)