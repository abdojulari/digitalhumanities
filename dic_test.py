import pandas as pd
import datetime
#import pandas.io.data
from pandas_datareader import data, wb
import csv

out= open("testfile.csv", "rb")
data = csv.reader(out)
#df = pd.read_csv('testfile.csv')
data = [[row[0],row[1] + row[2],row[3] + row[4], row[5],row[6]] for row in data]
out.close()
print data

out=open("data.csv", "wb")
output = csv.writer(out)

for row in data:
    output.writerow(row)

out.close()

df = pd.read_csv('data.csv')
for DateDpt, DateAr in df.iteritems():
	df.DateDpt = pd.to_datetime(df.DateDpt, format='%Y-%m-%d')
	df.DateAr = pd.to_datetime(df.DateAr, format='%Y-%m-%d')
print df


#d= df.set_index('Date').T.to_dict().values()



	
#Use collections.defaultdict for this. You can initialize a dictionary like "travel_dict = defaultdict(lambda: defaultdict(list))", then add values like "travel_dict["ParisFrance"]["2001-02-01"].append(1922)" 


