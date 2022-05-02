import os
from unittest import result
from numpy import pad
import pandas
import glob
import csv 
class MyTemplate:
    def __init__(self,shop_name,brand,model,price,date):
        self.shop_name = shop_name
        self.brand = brand
        self.model = model
        self.price = price
        self.date = date
# list of directory name
paths = ['./Shop A/','./Shop B/','./Shop C/']
list = []
outputFilePath = 'result.csv'
for path in paths:
    # print(path)
    for file in os.listdir(path):
        if file.endswith(".csv"):
            csv = pandas.read_csv(os.path.join(path ,file))
            # print(csv['Price'].str.isnumeric() == True)
            csv.to_csv('result.csv', index=False)
        if file.endswith(".xlsx"):
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=None,usecols='D:G')
            df = pandas.DataFrame(worksheet.items())
            print(df)
            df.to_csv('result.csv',mode='a')
    
