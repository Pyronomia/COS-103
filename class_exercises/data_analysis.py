import numpy as np
import pandas as pd
scores = np.array([68,72,8,32,12])
print(scores.mean())
print(scores.max())
print(scores + 5)

scores2 = pd.Series([12,65,43,98,72], name = 'score')
print(scores2[3])
# pandas still performs normal numpy maths

data = {'name': ['Ada', 'Bayo', 'Chika'],
        'score': [68, 91, 74]}

df = pd.DataFrame(data)
print(df)
print(df['score'])
print(df.loc[1])

df2 = pd.read_csv('./csv_files/Iris.csv')

# Common options you'll reach for:
print(pd.read_csv('./csv_files/CS Chess Players.csv', sep=';'))
# ^ use ';' as the delimiter
df3 =  pd.read_csv('./csv_files/CS Chess Players.csv', index_col = 0)
print(df3.loc["Chuks Smith", 'Age'])
# ^ use column 0 as the index: this means that the first column becomes the index used for searching. So if the first column is name, name is what is going to be used for searching. The column does not appear when you want to print the whole table

print(df2.head()) # shows the first 5 rows, for first ten you can use df2.head(10)
print(df2.tail()) # shows the last 5 rows
print(df2.shape) # gives no of rows, columns
print(df2.columns) # gives the names of all the columns

print(df2.info()) # info(): column names, types, and non-null counts — great for spotting missing data early
print(df2.describe()) # describe(): mean, std, min/max, and percentiles for every numeric column



