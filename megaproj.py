import pandas as pd
#from pandas import DataFrame 

import datetime
import pandas.io.data
from pandas_datareader import data, wb

df = pd.read_csv('testfile.csv')
grouped = df.groupby(['Date','Time'])
for name, group in grouped:
	print (name)
	print(group)

#for index, row in df.interrows():
#print (row['AuthorID'], row['Arrival'], row['Departure'], row['Date'], row['Time']) 


