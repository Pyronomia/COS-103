import pandas as pd

df = pd.read_csv('Sax Instrumentalists.csv')

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

print(df['Age'].mean()) # It is case sensitive
print(df['Age'].unique()) 
print(df.isnull()) 
print(df.isnull().sum()) 
print(df.isnull().sum().sum()) 
print(df.dropna()) 
print(df.dropna(subset=['Age'])) 
