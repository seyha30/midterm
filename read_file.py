import os
import pandas
import glob
import csv
paths = ['./Shop A/','./Shop B/','./Shop C/']
outputFilePath = 'result.csv'
for path in paths:
    print(path)
    for file in os.listdir(path):
        if file.endswith(".csv"):
            csv = pandas.read_csv(os.path.join(path ,file))
            print(csv)
        if file.endswith(".xlsx"):
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=None)
            print(worksheet)
            # print(file)