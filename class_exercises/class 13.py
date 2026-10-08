import pandas as pd

df = pd.read_csv('./csv_files/CS Chess Players.csv')

# Take any Data frame and report how many missing values are in each column
print(df.isnull().sum())

# Remove duplicate rows from a dataset, keeping only the first occurence
df = df.drop_duplicates()
print(df)

# Filter a dataset to rows matching two conditions at once
print(df[(df['Age'] >= 17) & (df["Gender"] ==  "Male")])

# Use groupby() to find the average of one column, grouped by another
print(f"The average of Elo Rating grouped by gender is:\n{df.groupby('Gender')['Elo Rating'].mean()}") 
