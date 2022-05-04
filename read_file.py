import os
import pandas
import csv
# list of directory name
paths = ['./Shop A/','./Shop B/','./Shop C/']
output_file = 'result.csv'
# remove existing content
file = open(output_file,'r+')
file.truncate(0)
file.close()
# 
for path in paths:
    for file in os.listdir(path):
        if file.endswith(".csv"):
            data = pandas.DataFrame()
            df= pandas.read_csv(os.path.join(path ,file))
            data = pandas.concat([data,df])
            # print(csv['Price'].str.isnumeric() == True)
            df.to_csv(output_file,mode='a')
            # for index , row in data.iterrows():
            #     print(row["Laptop Brand"] + '' + row["Laptop Model"]+ '' + row["Date"]+ '' + str(row["Price"])  )
        if file.endswith(".xlsx"):
            # data =  pandas.DataFrame(columns=['Shop Name','Brand','Model','Price'])
            data =  pandas.DataFrame()
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=0,usecols='D:G')
            # df = pandas.DataFrame(worksheet.items())
            data = pandas.concat([data,worksheet])
            # print(data)
            # df.to_csv(output_file, mode='a', index=True, header=True)
            data.to_csv(output_file,mode='a', index=False, header=False)
    
