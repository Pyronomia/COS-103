import pandas as pd

df = pd.read_csv('./csv_files/Sax Instrumentalists.csv')

# print(df.head())
# print(df.shape)
# print(df.info())

scores = pd.Series([21,77,89,32,54,61], name = 'score')
# print(scores.mean())
# print(scores.max())

data = {'name': ["Paul", "David", "Sarah"],
        'age': [67, 12, 32],
        'gender': ['Male', "Male", "Female"]}

# print(pd.DataFrame(data))

df2 = pd.read_csv('./csv_files/CS Chess Players.csv')

print(df['Age'].mean()) # It is case sensitive
print(df['Age'].unique()) # it is for a specific column and not the full dataset
print(df.isnull()) 
print(df.isnull().sum()) 
print(df.isnull().sum().sum()) 
print(df.dropna()) # this drops a row that has a null value
print(df.dropna(subset=['Age'])) 
print(df2['Age'].fillna(15)) # this fills in 15 as a fixed value for any missing values
print(df2['Age'].fillna(df2['Age'].mean())) # I guess this is a more practical approach of doing this by using the mean instead of a random value

print(df2.duplicated())
print(df2.duplicated().sum())

# FIXING DATA TYPES
print(df2.dtypes)
# price object <- stuck as text!

# Conversion to different datatypes
df2['Age'] = df['Age'].astype(float)
# df['date'] = pd.to_datetime(df['date'])

print(df.loc[3]) # row labeled 3
print(df.loc[3, 'Name of sax players']) # one cell, by label
print(df.loc[0:2, 'Name of sax players']) # rows 0-2, inclusive
print(df.iloc[3]) # row at position 3
print(df.iloc[0:2, 1]) # rows 0-1, by position 

# Filtering Boolean Indexing
print(df['Age'] > 18) # a True/False Series
print(df[df['Age'] > 18]) # rows where True
print(df[(df['Age'] > 18) & (df['Preferred sax'] == 'Soprano')])
df[df['Name of sax players'].isin(['Ada', 'Bayo'])]

print(df.sort_values('Age')) # ascending
print(df.sort_values('Age', ascending=False)) 
# NOTE: the actual dataframe will not change unless you reassign it
print(df.sort_index()) # sorts by row index

# CREATING NEW COLUMNS
df['Adult'] = df['Age'].apply(
 lambda s: 'Adult' if s >= 20 else 'Minor'
)

print(df)

# MERGING 2 tables together
students = pd.DataFrame(
 {'id': [1, 2], 'name': ['Ada', 'Bo']})
scores = pd.DataFrame(
 {'id': [1, 2], 'score': [88, 75]})

print(pd.merge(students, scores, on='id'))

print(df["Age"].unique())

line_count = len(df)# gives number of rows

df2 = pd.read_csv("./csv_files/manual_text.txt", sep = "\t", header=None, names=["line_text"], keep_default_na=False)

# 2. Counts apply directly to that single text column
line_count = len(df2)
word_count = df2["line_text"].str.split().str.len().sum()
char_count = df2["line_text"].str.len().sum()

print(f"Lines: {line_count} | Words: {word_count} | Characters: {char_count}")
print(line_count)
