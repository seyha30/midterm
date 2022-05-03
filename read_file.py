import os
import pandas
# list of directory name
paths = ['./Shop A/','./Shop B/','./Shop C/']
outputFilePath = 'result.csv'
# remove existing content
file = open(outputFilePath,'r+')
file.truncate(0)
file.close()
# 
for path in paths:
    for file in os.listdir(path):
        if file.endswith(".csv"):
            df= pandas.read_csv(os.path.join(path ,file))
            # print(csv['Price'].str.isnumeric() == True)
            df.to_csv(outputFilePath,mode='a')
        if file.endswith(".xlsx"):
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=None,usecols='D:G')
            df = pandas.DataFrame(worksheet.items())
            print(df.index)
            # for index, row in df.iterrows():
            #     print (row["Date"], row["Price"])
            df.to_csv(outputFilePath, mode='a', index=True, header=True)
    
