import os
import pandas
# list of directory name
paths = ['./Shop A/','./Shop B/','./Shop C/']
output_file = 'output.csv'
# remove existing csv content 
file = open(output_file,'r+')
file.truncate(0)
file.close()
# iterate files in directory
for path in paths:
    for file in os.listdir(path):
        if file.endswith(".csv"):
            df= pandas.read_csv(os.path.join(path ,file))
            # drop unused columns
            df = df.drop(columns=['No', 'Customer Name', 'Customer Phone No'])
            df.insert(loc=0,column='Shop Name',value=path)
            df.to_csv(output_file,mode='a' , index=False,header=False)
        if file.endswith(".xlsx"):
            data =  pandas.DataFrame()
            worksheet = pandas.read_excel(os.path.join(path ,file), sheet_name=0,usecols='D:G')
            data = pandas.concat([data,worksheet])
            # split column where its value contain '-'
            # data.Name.str.split(expand=True)
            print(data)
            data.insert(loc=0,column='Shop Name',value=path)
            data.to_csv(output_file,mode='a', index=False, header=False)

# 1-re-read result & modify
# 2-create dataframe with header template
# 3-calculate average
# 4-re-write to csv
df = pandas.read_csv(output_file)
print(df)
    
