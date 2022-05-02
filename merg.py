import pandas
import os
import csv
import re
import glob
dataDirectoryShopA = os.path.join('./Shop A/','*.xlsx')
dataDirectoryShopB = os.path.join('./Shop B/','*.xlsx')
dataDirectoryShopC = os.path.join('./Shop C/','*.xlsx')
outputFilePath = 'result.csv'
csvReader = open(outputFilePath,'w')
filePathA = glob.glob(dataDirectoryShopA)
filePathB = glob.glob(dataDirectoryShopB)
filePathC = glob.glob(dataDirectoryShopC)
data = pandas.DataFrame()
for filePath in filePathA:
    worksheet = pandas.read_excel(filePath, sheet_name=None )
    print(type(data))
    # data = pandas.concat([data, worksheet])
    print(worksheet)
for filePath in filePathB:
    worksheet = pandas.read_excel(filePath, sheet_name=None )
print(type(data))
# data = pandas.concat([data, worksheet])
print(worksheet)
for filePath in filePathC:
    worksheet = pandas.read_excel(filePath, sheet_name=None)
print(type(data))
# data = pandas.concat([data, worksheet])
print(worksheet)

    