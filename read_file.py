import os
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
    print(path)
    for file in os.listdir(path):
        if file.endswith(".csv"):
            csv = pandas.read_csv(os.path.join(path ,file))
            print(csv)
        if file.endswith(".xlsx") or file.endswith(".xls"):
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=None)
            print(worksheet)
# iterate list
for i in list:
    pass
# function for read csv file
def todo_read_csv():
    pass
# function for read excel file
def todo_read_excel():
    pass