import os
import pandas as pd

CSV_Path = os.path.join('hoppers.csv')
cols = ["x", "y", "date", "loc", "area"]
df = pd.read_csv(CSV_Path, skiprows = 12500, nrows=12500, index_col=0, usecols=[0,1,2,4,5], names = cols)

df[['date','time']] = df.date.str.split(" ",expand=True,)
df.index = pd.to_datetime(df['date'],format='%m/%d/%y') #sets index to date in DT format


mydf = df.groupby(df.index).size().reset_index()
mydf.rename(columns = {0: 'frequency'}, inplace = True)

print(mydf)
mydf.to_csv('hopperfreq.csv')

